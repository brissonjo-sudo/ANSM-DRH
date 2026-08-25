"""Tests de la suite d'évaluation comportementale."""

from copy import deepcopy
import json
from pathlib import Path
import unittest

from scripts.behavior_eval import build_review, validate_suite


PROJECT = Path(__file__).resolve().parents[1]


class BehaviorEvaluationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.suite = json.loads(
            (PROJECT / "evals" / "behavior-cases.json").read_text(encoding="utf-8")
        )

    def test_suite_is_valid_and_has_twenty_cases(self) -> None:
        self.assertEqual([], validate_suite(self.suite))
        self.assertEqual(20, len(self.suite["cases"]))

    def test_unknown_branch_is_rejected(self) -> None:
        suite = deepcopy(self.suite)
        suite["cases"][0]["branches"] = ["references/inconnue.md"]
        self.assertTrue(any("branches inconnues" in item for item in validate_suite(suite)))

    def test_duplicate_case_id_is_rejected(self) -> None:
        suite = deepcopy(self.suite)
        suite["cases"][1]["id"] = suite["cases"][0]["id"]
        self.assertTrue(any("dupliqué" in item for item in validate_suite(suite)))

    def test_forbidden_claim_requests_semantic_review(self) -> None:
        case = self.suite["cases"][0]
        review = build_review(case, "Il existe une interdiction automatique de trois ans.")
        self.assertEqual("review", review["automatic_gate"])
        self.assertEqual(1, len(review["forbidden_claims_found"]))

    def test_safe_response_still_requires_semantic_review(self) -> None:
        case = self.suite["cases"][0]
        review = build_review(case, "Une analyse individualisée est nécessaire.")
        self.assertEqual("clear", review["automatic_gate"])
        self.assertTrue(all(item["result"] == "to_review" for item in review["manual_criteria"]))


if __name__ == "__main__":
    unittest.main()
