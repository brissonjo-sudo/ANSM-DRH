"""Validation et préparation des revues comportementales du skill."""

from __future__ import annotations

from argparse import ArgumentParser
import json
from pathlib import Path
import re
import sys

try:
    from .source_gate import BRANCH_FILES
except ImportError:  # Exécution directe depuis scripts/
    from source_gate import BRANCH_FILES


VALID_SENSITIVITY = {"ordinary", "personal", "health", "disciplinary", "ethics"}
VALID_CONTEXT = {
    "agent_category",
    "direction",
    "site",
    "ethics_exposure",
    "deadline",
    "documents",
}


def validate_suite(suite: object) -> list[str]:
    """Retourne les erreurs structurelles d'une suite d'évaluation."""
    errors: list[str] = []
    if not isinstance(suite, dict):
        return ["La suite doit être un objet JSON."]
    if suite.get("version") != 2:
        errors.append("La version de la suite doit être 2.")
    cases = suite.get("cases")
    if not isinstance(cases, list):
        return errors + ["Le champ cases doit être une liste."]
    if not 15 <= len(cases) <= 30:
        errors.append("La suite doit contenir entre 15 et 30 scénarios.")

    case_ids: set[str] = set()
    covered_branches: set[str] = set()
    cross_branch_cases = 0
    sensitive_cases = 0

    for index, case in enumerate(cases, start=1):
        prefix = f"Cas #{index}"
        if not isinstance(case, dict):
            errors.append(f"{prefix} doit être un objet.")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not re.fullmatch(r"[a-z0-9-]+", case_id):
            errors.append(f"{prefix} : identifiant invalide.")
            case_id = f"index-{index}"
        elif case_id in case_ids:
            errors.append(f"{prefix} : identifiant dupliqué {case_id}.")
        case_ids.add(case_id)
        prefix = case_id

        prompt = case.get("prompt")
        if not isinstance(prompt, str) or len(prompt.strip()) < 20:
            errors.append(f"{prefix} : prompt trop court ou absent.")

        branches = case.get("branches")
        if not isinstance(branches, list) or not branches:
            errors.append(f"{prefix} : au moins une branche est requise.")
            branches = []
        else:
            unknown = set(branches) - BRANCH_FILES
            if unknown:
                errors.append(f"{prefix} : branches inconnues {sorted(unknown)}.")
            covered_branches.update(set(branches) & BRANCH_FILES)
            if len(set(branches)) > 1:
                cross_branch_cases += 1

        context = case.get("required_context")
        if not isinstance(context, list) or any(item not in VALID_CONTEXT for item in context):
            errors.append(f"{prefix} : required_context invalide.")

        sensitivity = case.get("sensitivity")
        if sensitivity not in VALID_SENSITIVITY:
            errors.append(f"{prefix} : sensibilité invalide.")
        elif sensitivity != "ordinary":
            sensitive_cases += 1

        criteria = case.get("criteria")
        if not isinstance(criteria, list) or not criteria:
            errors.append(f"{prefix} : critères métier manquants.")
        else:
            criterion_ids: set[str] = set()
            for criterion in criteria:
                if not isinstance(criterion, dict):
                    errors.append(f"{prefix} : critère invalide.")
                    continue
                criterion_id = criterion.get("id")
                description = criterion.get("description")
                if not isinstance(criterion_id, str) or not re.fullmatch(r"[a-z0-9-]+", criterion_id):
                    errors.append(f"{prefix} : identifiant de critère invalide.")
                elif criterion_id in criterion_ids:
                    errors.append(f"{prefix} : critère dupliqué {criterion_id}.")
                criterion_ids.add(criterion_id)
                if not isinstance(description, str) or len(description.strip()) < 12:
                    errors.append(f"{prefix}/{criterion_id} : description insuffisante.")
                if not isinstance(criterion.get("critical"), bool):
                    errors.append(f"{prefix}/{criterion_id} : critical doit être booléen.")

        forbidden = case.get("forbidden_claims")
        if not isinstance(forbidden, list) or any(not isinstance(item, str) or not item.strip() for item in forbidden):
            errors.append(f"{prefix} : forbidden_claims doit être une liste de textes.")

    missing = BRANCH_FILES - covered_branches
    if missing:
        errors.append(f"Branches sans scénario : {sorted(missing)}.")
    if cross_branch_cases < 4:
        errors.append("Au moins quatre scénarios inter-branches sont requis.")
    if sensitive_cases < 4:
        errors.append("Au moins quatre scénarios sensibles sont requis.")
    return errors


def find_forbidden_claims(case: dict, response: str) -> list[str]:
    """Repère lexicalement les formulations critiques à examiner."""
    normalized = " ".join(response.casefold().split())
    return [
        claim
        for claim in case.get("forbidden_claims", [])
        if " ".join(claim.casefold().split()) in normalized
    ]


def build_review(case: dict, response: str) -> dict:
    """Construit une grille de revue ; les critères restent à évaluer sémantiquement."""
    forbidden = find_forbidden_claims(case, response)
    return {
        "case_id": case["id"],
        "automatic_gate": "review" if forbidden else "clear",
        "forbidden_claims_found": forbidden,
        "manual_criteria": [
            {
                "id": criterion["id"],
                "critical": criterion["critical"],
                "description": criterion["description"],
                "result": "to_review",
            }
            for criterion in case["criteria"]
        ],
        "review_note": (
            "Une alerte lexicale doit être interprétée dans son contexte, "
            "notamment en présence d'une négation. Elle ne remplace pas "
            "l'évaluation sémantique des critères métier."
        ),
    }


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = ArgumentParser(description="Valide ou prépare une revue comportementale.")
    parser.add_argument("--suite", type=Path, default=root / "evals" / "behavior-cases.json")
    parser.add_argument("--case")
    parser.add_argument("--response", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    suite = json.loads(args.suite.read_text(encoding="utf-8"))
    errors = validate_suite(suite)
    if errors:
        print("ÉCHEC")
        for error in errors:
            print(f"- {error}")
        return 1
    if not args.case:
        print(f"OK — {len(suite['cases'])} scénarios comportementaux valides.")
        return 0
    if args.response is None:
        parser.error("--response est requis avec --case")
    case = next((item for item in suite["cases"] if item["id"] == args.case), None)
    if case is None:
        parser.error(f"cas inconnu : {args.case}")
    review = build_review(case, args.response.read_text(encoding="utf-8"))
    rendered = json.dumps(review, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 2 if review["automatic_gate"] == "review" else 0


if __name__ == "__main__":
    sys.exit(main())
