"""Tests du préavis d'expiration des sources."""

from datetime import date
import unittest

from scripts.freshness_report import build_report, render_markdown


MANIFEST = {
    "branches": {
        "references/test.md": {
            "claims": [
                {
                    "id": "claim-test",
                    "checked_on": "2026-01-01",
                    "max_age_days": 30,
                }
            ]
        }
    }
}

# Échéance synthétique : 31 janvier 2026. Ces sondes vérifient les bornes
# exactes sans dépendre des campagnes de vérification du registre réel.
BEFORE_WINDOW = date(2026, 1, 23)  # 8 jours restants : ok
INSIDE_WINDOW = date(2026, 1, 24)  # 7 jours restants : warning
AFTER_EXPIRY = date(2026, 2, 1)  # 1 jour de retard : expired


class FreshnessReportTests(unittest.TestCase):
    def test_report_is_ok_before_warning_window(self) -> None:
        report = build_report(MANIFEST, BEFORE_WINDOW, warning_days=7)
        self.assertEqual("ok", report["state"])
        self.assertEqual([], report["items"])

    def test_report_warns_seven_days_before_expiry(self) -> None:
        report = build_report(MANIFEST, INSIDE_WINDOW, warning_days=7)
        self.assertEqual("warning", report["state"])
        self.assertEqual(1, len(report["items"]))
        self.assertEqual(7, report["items"][0]["days_remaining"])
        self.assertEqual("warning", report["items"][0]["state"])

    def test_report_marks_expired_claims(self) -> None:
        report = build_report(MANIFEST, AFTER_EXPIRY, warning_days=7)
        self.assertEqual("expired", report["state"])
        self.assertEqual(-1, report["items"][0]["days_remaining"])
        self.assertEqual("expired", report["items"][0]["state"])

    def test_markdown_contains_actionable_deadline(self) -> None:
        report = build_report(MANIFEST, INSIDE_WINDOW, warning_days=7)
        markdown = render_markdown(report)
        self.assertIn("Échéance", markdown)
        self.assertIn("checked_on", markdown)


if __name__ == "__main__":
    unittest.main()
