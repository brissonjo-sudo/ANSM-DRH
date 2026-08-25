"""Validation du registre de besoins en sources internes."""

from __future__ import annotations

from argparse import ArgumentParser
from datetime import date
import json
from pathlib import Path
import re
import sys


INCOMPLETE_BRANCHES = {
    "references/deontologie-conflits-interets.md",
    "references/masse-salariale-budget-sirh.md",
    "references/qvt-sante-travail.md",
    "references/formation-developpement-competences.md",
    "references/communication-interne.md",
}
VALID_STATUS = {"missing", "received", "reviewed", "integrated"}
FORBIDDEN_KEYS = {"content", "text", "local_path", "personal_data", "attachment"}


def validate_requirements(registry: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(registry, dict):
        return ["Le registre interne doit être un objet JSON."]
    if registry.get("version") != 1:
        errors.append("La version du registre interne doit être 1.")
    if registry.get("repository_policy") != "metadata-only-no-confidential-content":
        errors.append("La politique metadata-only-no-confidential-content est obligatoire.")
    requirements = registry.get("requirements")
    if not isinstance(requirements, list):
        return errors + ["Le champ requirements doit être une liste."]

    seen_ids: set[str] = set()
    covered: set[str] = set()
    for index, item in enumerate(requirements, start=1):
        prefix = f"Besoin #{index}"
        if not isinstance(item, dict):
            errors.append(f"{prefix} doit être un objet.")
            continue
        forbidden = FORBIDDEN_KEYS & set(item)
        if forbidden:
            errors.append(f"{prefix} contient des champs interdits : {sorted(forbidden)}.")
        item_id = item.get("id")
        if not isinstance(item_id, str) or not re.fullmatch(r"[a-z0-9-]+", item_id):
            errors.append(f"{prefix} : identifiant invalide.")
        elif item_id in seen_ids:
            errors.append(f"{prefix} : identifiant dupliqué {item_id}.")
        seen_ids.add(item_id)
        branch = item.get("branch")
        if branch not in INCOMPLETE_BRANCHES:
            errors.append(f"{prefix} : branche inconnue ou déjà fiabilisée.")
        else:
            covered.add(branch)
        for key in ("title", "owner"):
            if not isinstance(item.get(key), str) or not item[key].strip():
                errors.append(f"{prefix} : {key} manquant.")
        status = item.get("status")
        if status not in VALID_STATUS:
            errors.append(f"{prefix} : statut invalide.")
        if status in {"received", "reviewed", "integrated"}:
            if not isinstance(item.get("secure_reference"), str) or not item["secure_reference"].strip():
                errors.append(f"{prefix} : secure_reference requis au statut {status}.")
        if status in {"reviewed", "integrated"}:
            for key in ("version_label", "reviewed_on"):
                if not isinstance(item.get(key), str) or not item[key].strip():
                    errors.append(f"{prefix} : {key} requis au statut {status}.")
            if isinstance(item.get("reviewed_on"), str):
                try:
                    date.fromisoformat(item["reviewed_on"])
                except ValueError:
                    errors.append(f"{prefix} : reviewed_on invalide.")

    missing = INCOMPLETE_BRANCHES - covered
    if missing:
        errors.append(f"Branches incomplètes sans plan d'acquisition : {sorted(missing)}.")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = ArgumentParser(description="Valide le suivi des sources internes manquantes.")
    parser.add_argument(
        "--registry",
        type=Path,
        default=root / "evals" / "internal-source-requirements.json",
    )
    args = parser.parse_args()
    try:
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ÉCHEC — {exc}")
        return 1
    errors = validate_requirements(registry)
    if errors:
        print("ÉCHEC")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK — {len(registry['requirements'])} besoins internes suivis sans contenu confidentiel.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
