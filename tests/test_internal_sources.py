"""Tests du registre de sources internes."""

from copy import deepcopy
import json
from pathlib import Path
import unittest

from scripts.internal_sources import validate_requirements


PROJECT = Path(__file__).resolve().parents[1]


class InternalSourcesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.registry = json.loads(
            (PROJECT / "evals" / "internal-source-requirements.json").read_text(encoding="utf-8")
        )

    def test_current_registry_is_valid(self) -> None:
        self.assertEqual([], validate_requirements(self.registry))

    def test_confidential_content_field_is_rejected(self) -> None:
        registry = deepcopy(self.registry)
        registry["requirements"][0]["content"] = "texte interne"
        self.assertTrue(any("champs interdits" in item for item in validate_requirements(registry)))

    def test_each_incomplete_branch_must_be_covered(self) -> None:
        registry = deepcopy(self.registry)
        registry["requirements"] = [
            item for item in registry["requirements"]
            if item["branch"] != "references/communication-interne.md"
        ]
        self.assertTrue(any("sans plan d'acquisition" in item for item in validate_requirements(registry)))

    def test_reviewed_source_requires_traceability_metadata(self) -> None:
        registry = deepcopy(self.registry)
        registry["requirements"][0]["status"] = "reviewed"
        errors = validate_requirements(registry)
        self.assertTrue(any("secure_reference" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
