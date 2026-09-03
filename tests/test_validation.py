"""Tests en mémoire de la barrière de fiabilisation."""

from copy import deepcopy
from datetime import date, timedelta
import json
from pathlib import Path
import unittest

from scripts.source_gate import BRANCH_FILES, parse_registry, validate_source_gates


PROJECT = Path(__file__).resolve().parents[1]
# Date de référence des tests : elle suit la dernière vérification de
# sources du dépôt. Une affirmation contrôlée après cette date serait vue
# comme « située dans le futur » — remonter TODAY en même temps qu'une
# campagne de vérification, jamais pour contourner un contrôle.
TODAY = date(2026, 9, 3)
CONTRACTUELS = "references/recrutement-classification-contractuels.md"
DEONTOLOGIE = "references/deontologie-conflits-interets.md"


class ValidationGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.gates = json.loads(
            (PROJECT / "evals" / "source-gates.json").read_text(encoding="utf-8")
        )
        cls.registry = parse_registry(
            (PROJECT / "references" / "sources-principales.md").read_text(encoding="utf-8")
        )
        cls.branches = {
            branch: (PROJECT / branch).read_text(encoding="utf-8")
            for branch in BRANCH_FILES
        }

    def validate(self, *, gates=None, registry=None, branches=None) -> list[str]:
        return validate_source_gates(
            deepcopy(self.gates if gates is None else gates),
            deepcopy(self.registry if registry is None else registry),
            deepcopy(self.branches if branches is None else branches),
            TODAY,
        )

    def assert_blocked(self, expected_fragment: str, **kwargs) -> None:
        errors = self.validate(**kwargs)
        self.assertTrue(
            any(expected_fragment in error for error in errors),
            f"Erreur attendue absente : {expected_fragment!r}\nErreurs : {errors}",
        )

    def test_current_repository_passes(self) -> None:
        self.assertEqual([], self.validate())

    def test_first_of_month_is_written_1er(self) -> None:
        # « vérification du 1 septembre » n'est pas du français : le formateur
        # doit produire « 1er ». Sans ce cas, une branche vérifiée un premier
        # du mois ne peut pas passer la barrière.
        branches = deepcopy(self.branches)
        gates = deepcopy(self.gates)
        gates["branches"][CONTRACTUELS]["verified_on"] = "2026-09-01"
        for claim in gates["branches"][CONTRACTUELS]["claims"]:
            claim["checked_on"] = "2026-09-01"
        branches[CONTRACTUELS] = branches[CONTRACTUELS].replace(
            "vérification du 25 août 2026", "vérification du 1er septembre 2026", 1
        )
        self.assertEqual([], self.validate(gates=gates, branches=branches))

    def test_missing_source_is_blocked(self) -> None:
        gates = deepcopy(self.gates)
        gates["branches"][CONTRACTUELS]["claims"][0]["source_ids"] = ["SOURCE-INCONNUE"]
        self.assert_blocked("source absente", gates=gates)

    def test_unofficial_domain_is_blocked(self) -> None:
        registry = deepcopy(self.registry)
        registry["CONTRACTUELS-ANSM"] = "https://example.com/source"
        self.assert_blocked("domaine non officiel", registry=registry)

    def test_branch_date_mismatch_is_blocked(self) -> None:
        branches = deepcopy(self.branches)
        branches[CONTRACTUELS] = branches[CONTRACTUELS].replace(
            "vérification du 25 août 2026", "vérification du 24 août 2026"
        )
        self.assert_blocked("date de la branche", branches=branches)

    def test_unresolved_point_on_verified_branch_is_blocked(self) -> None:
        gates = deepcopy(self.gates)
        gates["branches"][CONTRACTUELS]["unresolved_claims"] = ["Question non résolue"]
        self.assert_blocked("ne peut avoir", gates=gates)

    def test_missing_branch_is_blocked(self) -> None:
        gates = deepcopy(self.gates)
        del gates["branches"][CONTRACTUELS]
        self.assert_blocked("8 branches", gates=gates)

    def test_expired_claim_is_blocked(self) -> None:
        gates = deepcopy(self.gates)
        gates["branches"][DEONTOLOGIE]["claims"][0]["checked_on"] = "2026-07-01"
        self.assert_blocked("source expirée", gates=gates)

    def test_future_check_date_is_blocked(self) -> None:
        gates = deepcopy(self.gates)
        demain = (TODAY + timedelta(days=1)).isoformat()
        gates["branches"][DEONTOLOGIE]["claims"][0]["checked_on"] = demain
        self.assert_blocked("futur", gates=gates)


if __name__ == "__main__":
    unittest.main()
