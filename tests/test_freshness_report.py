"""Tests du préavis d'expiration des sources."""

from datetime import date
import json
from pathlib import Path
import unittest

from scripts.freshness_report import build_report, render_markdown


PROJECT = Path(__file__).resolve().parents[1]


class FreshnessReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = json.loads(
            (PROJECT / "evals" / "source-gates.json").read_text(encoding="utf-8")
        )

    def test_report_is_ok_before_warning_window(self) -> None:
        report = build_report(self.manifest, date(2026, 9, 1), warning_days=7)
        self.assertEqual("ok", report["state"])
        self.assertEqual([], report["items"])

    def test_report_warns_seven_days_before_expiry(self) -> None:
        report = build_report(self.manifest, date(2026, 9, 18), warning_days=7)
        self.assertEqual("warning", report["state"])
        self.assertTrue(report["items"])
        self.assertTrue(all(item["days_remaining"] <= 7 for item in report["items"]))

    def test_report_marks_expired_claims(self) -> None:
        report = build_report(self.manifest, date(2026, 9, 25), warning_days=7)
        self.assertEqual("expired", report["state"])
        self.assertTrue(any(item["days_remaining"] < 0 for item in report["items"]))

    def test_markdown_contains_actionable_deadline(self) -> None:
        report = build_report(self.manifest, date(2026, 9, 18), warning_days=7)
        markdown = render_markdown(report)
        self.assertIn("Échéance", markdown)
        self.assertIn("checked_on", markdown)


if __name__ == "__main__":
    unittest.main()
