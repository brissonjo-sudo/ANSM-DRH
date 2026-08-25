"""Tests du filtre local de données RH."""

import unittest

from scripts.privacy_scan import exit_code_for_findings, redact_text, scan_text


class PrivacyScanTests(unittest.TestCase):
    def test_generic_hr_request_is_clean(self) -> None:
        self.assertEqual([], scan_text("Comment organiser une campagne de formation ?"))

    def test_direct_identifiers_are_detected_without_echoing_values(self) -> None:
        text = "Contact : agent@example.fr, 06 12 34 56 78, matricule AB-1234."
        findings = scan_text(text)
        kinds = {item["kind"] for item in findings}
        self.assertTrue({"email", "telephone", "matricule"}.issubset(kinds))
        self.assertNotIn("agent@example.fr", str(findings))
        self.assertEqual(1, exit_code_for_findings(findings))

    def test_nir_and_iban_are_high_risk(self) -> None:
        text = "NIR 1 84 12 75 123 456 78 et IBAN FR76 3000 6000 0112 3456 7890 189."
        findings = scan_text(text)
        high_kinds = {item["kind"] for item in findings if item["severity"] == "high"}
        self.assertTrue({"nir", "iban"}.issubset(high_kinds))
        self.assertEqual(2, exit_code_for_findings(findings))

    def test_sensitive_identified_case_is_escalated(self) -> None:
        findings = scan_text("Dossier médical à transmettre à agent@example.fr.")
        self.assertTrue(any(item["kind"] == "identified_sensitive_case" for item in findings))
        self.assertEqual(2, exit_code_for_findings(findings))

    def test_sensitive_context_without_identifier_is_only_a_warning(self) -> None:
        findings = scan_text("Comment orienter une situation générique de souffrance au travail ?")
        self.assertEqual(0, exit_code_for_findings(findings))

    def test_redaction_replaces_identifiers(self) -> None:
        redacted = redact_text("Écrire à agent@example.fr ou au 06 12 34 56 78.")
        self.assertNotIn("agent@example.fr", redacted)
        self.assertNotIn("06 12 34 56 78", redacted)


if __name__ == "__main__":
    unittest.main()
