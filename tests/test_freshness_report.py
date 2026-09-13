"""Tests du préavis d'expiration des sources."""

from datetime import date, timedelta
import json
from pathlib import Path
import unittest

from scripts.freshness_report import build_report, render_markdown


PROJECT = Path(__file__).resolve().parents[1]

# Ces tests sondent le manifeste réel à des dates choisies de part et d'autre
# de l'échéance la plus proche, pour vérifier les transitions ok → warning →
# expired. Ils sont donc calibrés sur les données : toute campagne de
# vérification qui repousse un `checked_on` repousse aussi ces sondes, et il
# faut les recaler — jamais en élargissant la fenêtre pour faire passer un
# test, toujours en les replaçant autour de la nouvelle échéance la plus
# proche. Au 13 septembre 2026, celle-ci est le 1er octobre 2026
# (déontologie, contrôlée le 1er septembre, fenêtre de 30 jours).
# Une seule date à corriger lors d'un recalage : les trois sondes en dérivent.
EXPIRY_SOONEST = date(2026, 10, 1)
BEFORE_WINDOW = EXPIRY_SOONEST - timedelta(days=18)  # hors préavis
INSIDE_WINDOW = EXPIRY_SOONEST - timedelta(days=6)  # dans le préavis
AFTER_EXPIRY = EXPIRY_SOONEST + timedelta(days=1)  # expirée


class FreshnessReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(
            (PROJECT / "evals" / "source-gates.json").read_text(encoding="utf-8")
        )

    def test_report_is_ok_before_warning_window(self) -> None:
        report = build_report(self.manifest, BEFORE_WINDOW, warning_days=7)
        self.assertEqual("ok", report["state"])
        self.assertEqual([], report["items"])

    def test_report_warns_seven_days_before_expiry(self) -> None:
        report = build_report(self.manifest, INSIDE_WINDOW, warning_days=7)
        self.assertEqual("warning", report["state"])
        self.assertTrue(report["items"])
        self.assertTrue(all(item["days_remaining"] <= 7 for item in report["items"]))

    def test_report_marks_expired_claims(self) -> None:
        report = build_report(self.manifest, AFTER_EXPIRY, warning_days=7)
        self.assertEqual("expired", report["state"])
        self.assertTrue(any(item["days_remaining"] < 0 for item in report["items"]))

    def test_markdown_contains_actionable_deadline(self) -> None:
        report = build_report(self.manifest, INSIDE_WINDOW, warning_days=7)
        markdown = render_markdown(report)
        self.assertIn("Échéance", markdown)
        self.assertIn("checked_on", markdown)


if __name__ == "__main__":
    unittest.main()
