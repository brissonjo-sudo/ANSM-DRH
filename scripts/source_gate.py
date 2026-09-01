"""Logique pure de validation du manifeste de sources."""

from datetime import date
from urllib.parse import urlparse
import re


BRANCH_FILES = {
    "references/deontologie-conflits-interets.md",
    "references/recrutement-classification-contractuels.md",
    "references/instances-dialogue-social.md",
    "references/fonctionnaires-corps-specifiques.md",
    "references/masse-salariale-budget-sirh.md",
    "references/qvt-sante-travail.md",
    "references/formation-developpement-competences.md",
    "references/communication-interne.md",
}
MATURITY_MARKERS = {"✅": "verified", "🟢": "partial", "🟡": "draft"}
UNVERIFIED_TERMS = re.compile(r"à confirmer|non vérifi[ée]|source manquante", re.IGNORECASE)
OFFICIAL_HOSTS = {
    "ansm.sante.fr",
    "www.fonction-publique.gouv.fr",
    "www.legifrance.gouv.fr",
}
FRENCH_MONTHS = {
    1: "janvier", 2: "février", 3: "mars", 4: "avril",
    5: "mai", 6: "juin", 7: "juillet", 8: "août",
    9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre",
}


def parse_registry(content: str) -> dict[str, str]:
    return dict(re.findall(r"^\| `([^`]+)` \|.*?\| <(https://[^>]+)> \|", content, re.MULTILINE))


def validate_source_gates(
    source_gates: object,
    registry_sources: dict[str, str],
    branch_contents: dict[str, str],
    today: date,
) -> list[str]:
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    require(isinstance(source_gates, dict), "Barrière de fiabilisation : racine JSON invalide")
    if not isinstance(source_gates, dict):
        return errors

    branches = source_gates.get("branches", {})
    require(isinstance(branches, dict), "Barrière de fiabilisation : branches doit être un objet")
    if not isinstance(branches, dict):
        return errors
    require(set(branches) == BRANCH_FILES, "Barrière de fiabilisation : les 8 branches doivent être déclarées exactement")

    for branch_file in sorted(BRANCH_FILES):
        require(branch_file in branch_contents, f"Barrière de fiabilisation : branche introuvable {branch_file}")
        if branch_file not in branch_contents or branch_file not in branches:
            continue

        branch_content = branch_contents[branch_file]
        header = "\n".join(branch_content.splitlines()[:8])
        detected = next((value for marker, value in MATURITY_MARKERS.items() if marker in header), None)
        gate = branches[branch_file]
        require(isinstance(gate, dict), f"{branch_file} : configuration de barrière invalide")
        if not isinstance(gate, dict):
            continue
        require(detected is not None, f"{branch_file} : maturité absente de l'en-tête")
        require(gate.get("maturity") == detected, f"{branch_file} : maturité incohérente entre branche et barrière")

        verified_on = gate.get("verified_on")
        if verified_on is not None:
            try:
                verification_date = date.fromisoformat(verified_on)
                # Le premier jour du mois s'écrit « 1er » en français : sans ce
                # cas particulier, aucune branche vérifiée un 1er ne peut passer.
                french_day = "1er" if verification_date.day == 1 else str(verification_date.day)
                french_date = f"{french_day} {FRENCH_MONTHS[verification_date.month]} {verification_date.year}"
                require(f"vérification du {french_date}" in header, f"{branch_file} : date de la branche différente de verified_on")
            except (TypeError, ValueError):
                errors.append(f"{branch_file} : date verified_on invalide")

        claims = gate.get("claims", [])
        unresolved = gate.get("unresolved_claims", [])
        known_limits = gate.get("known_limits", [])
        require(isinstance(claims, list), f"{branch_file} : claims doit être une liste")
        require(isinstance(unresolved, list), f"{branch_file} : unresolved_claims doit être une liste")
        require(isinstance(known_limits, list), f"{branch_file} : known_limits doit être une liste")

        if detected == "verified":
            require(bool(verified_on), f"{branch_file} : une branche ✅ exige une date de vérification")
            require(bool(claims), f"{branch_file} : une branche ✅ exige au moins une affirmation importante")
            require(not unresolved, f"{branch_file} : une branche ✅ ne peut avoir d'affirmation importante non résolue")

        claim_ids: set[str] = set()
        claim_dates: list[date] = []
        for claim in claims if isinstance(claims, list) else []:
            claim_id = claim.get("id", "") if isinstance(claim, dict) else ""
            statement = claim.get("statement", "") if isinstance(claim, dict) else ""
            status = claim.get("status") if isinstance(claim, dict) else None
            checked_on = claim.get("checked_on") if isinstance(claim, dict) else None
            max_age_days = claim.get("max_age_days") if isinstance(claim, dict) else None
            source_ids = claim.get("source_ids", []) if isinstance(claim, dict) else []
            require(bool(re.fullmatch(r"[a-z0-9-]+", claim_id)), f"{branch_file} : identifiant d'affirmation invalide")
            require(claim_id not in claim_ids, f"{branch_file} : affirmation dupliquée {claim_id}")
            claim_ids.add(claim_id)
            require(bool(statement), f"{branch_file}/{claim_id} : formulation manquante")
            require(status == "verified", f"{branch_file}/{claim_id} : affirmation importante non vérifiée")
            require(not UNVERIFIED_TERMS.search(statement), f"{branch_file}/{claim_id} : formulation contient une réserve bloquante")
            require(max_age_days in {30, 90}, f"{branch_file}/{claim_id} : max_age_days doit valoir 30 ou 90")
            try:
                claim_date = date.fromisoformat(checked_on)
                claim_dates.append(claim_date)
                age_days = (today - claim_date).days
                require(age_days >= 0, f"{branch_file}/{claim_id} : date de contrôle située dans le futur")
                if max_age_days in {30, 90}:
                    require(age_days <= max_age_days, f"{branch_file}/{claim_id} : source expirée ({age_days} jours, maximum {max_age_days})")
            except (TypeError, ValueError):
                errors.append(f"{branch_file}/{claim_id} : date checked_on invalide")
            require(isinstance(source_ids, list) and bool(source_ids), f"{branch_file}/{claim_id} : identifiant de source manquant")
            for source_id in source_ids if isinstance(source_ids, list) else []:
                require(source_id in registry_sources, f"{branch_file}/{claim_id} : source absente ou sans URL officielle {source_id}")
                if source_id in registry_sources:
                    host = urlparse(registry_sources[source_id]).hostname
                    require(host in OFFICIAL_HOSTS, f"{branch_file}/{claim_id} : domaine non officiel pour {source_id}")
                    require(f"`{source_id}`" in branch_content, f"{branch_file}/{claim_id} : source {source_id} non citée dans la branche")

        if claim_dates and verified_on is not None:
            require(verified_on == max(claim_dates).isoformat(), f"{branch_file} : verified_on doit reprendre le contrôle le plus récent")

    return errors
