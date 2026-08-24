"""Contrôles légers, sans dépendance, pour la publication du skill."""

from pathlib import Path
from datetime import date
import json
import re
import sys
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []


def require(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


skill_path = ROOT / "SKILL.md"
skill = skill_path.read_text(encoding="utf-8")
require(skill.startswith("---\n"), "SKILL.md : frontmatter YAML manquant")

frontmatter_end = skill.find("\n---\n", 4)
require(frontmatter_end != -1, "SKILL.md : fin du frontmatter introuvable")
if frontmatter_end != -1:
    frontmatter = skill[4:frontmatter_end]
    body = skill[frontmatter_end + 5 :]
    name = re.search(r"^name:\s*([^\n]+)$", frontmatter, re.MULTILINE)
    require(name is not None, "SKILL.md : champ name manquant")
    if name:
        require(bool(re.fullmatch(r"[a-z0-9-]{1,64}", name.group(1).strip())), "SKILL.md : name doit être en kebab-case")
    description = re.search(r"^description:\s*>?-?\s*\n((?:^[ \t]+.*\n?)*)", frontmatter, re.MULTILINE)
    require(description is not None, "SKILL.md : champ description manquant")
    if description:
        description_text = " ".join(line.strip() for line in description.group(1).splitlines())
        require(len(description_text) <= 1024, "SKILL.md : description dépasse 1024 caractères")
    require(len(body.splitlines()) < 500, "SKILL.md : corps du skill doit rester sous 500 lignes")

require("[sourcé]" not in skill, "SKILL.md : balise [sourcé] non prise en charge")

for markdown in ROOT.rglob("*.md"):
    content = markdown.read_text(encoding="utf-8")
    for reference in re.findall(r"(?:references|assets)/[A-Za-z0-9_.-]+\.md", content):
        require((ROOT / reference).is_file(), f"{markdown.relative_to(ROOT)} : lien local introuvable {reference}")

for markdown in (ROOT / "references").glob("*.md"):
    content = markdown.read_text(encoding="utf-8")
    if len(content.splitlines()) > 100:
        require("## Repérage rapide" in content, f"{markdown.relative_to(ROOT)} : sommaire rapide manquant")

registry = ROOT / "references" / "sources-principales.md"
registry_sources: dict[str, str] = {}
require(registry.is_file(), "Registre des sources principales manquant")
if registry.is_file():
    registry_content = registry.read_text(encoding="utf-8")
    require("https://" in registry_content, "Registre des sources sans lien officiel")
    require("CGFP-ENTRANT" in registry_content, "Registre : contrôle déontologique entrant manquant")
    require("LFSS-DOTATION-2026" in registry_content, "Registre : source légale de la dotation 2026 manquante")
    require("ANSM-DEONTO-2023" in registry_content, "Registre : rapport public ANSM 2023 manquant")
    for source_id, url in re.findall(r"^\| `([^`]+)` \|.*?\| <(https://[^>]+)> \|", registry_content, re.MULTILINE):
        registry_sources[source_id] = url


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

source_gates_path = ROOT / "evals" / "source-gates.json"
require(source_gates_path.is_file(), "Barrière de fiabilisation evals/source-gates.json manquante")
if source_gates_path.is_file():
    try:
        source_gates = json.loads(source_gates_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f"Barrière de fiabilisation illisible : {exc}")
        source_gates = {"branches": {}}

    branches = source_gates.get("branches", {})
    require(isinstance(branches, dict), "Barrière de fiabilisation : branches doit être un objet")
    if not isinstance(branches, dict):
        branches = {}
    require(set(branches) == BRANCH_FILES, "Barrière de fiabilisation : les 8 branches doivent être déclarées exactement")

    for branch_file in sorted(BRANCH_FILES):
        branch_path = ROOT / branch_file
        require(branch_path.is_file(), f"Barrière de fiabilisation : branche introuvable {branch_file}")
        if not branch_path.is_file() or branch_file not in branches:
            continue

        branch_content = branch_path.read_text(encoding="utf-8")
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
                french_date = f"{verification_date.day} {FRENCH_MONTHS[verification_date.month]} {verification_date.year}"
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
        for claim in claims if isinstance(claims, list) else []:
            claim_id = claim.get("id", "") if isinstance(claim, dict) else ""
            statement = claim.get("statement", "") if isinstance(claim, dict) else ""
            status = claim.get("status") if isinstance(claim, dict) else None
            source_ids = claim.get("source_ids", []) if isinstance(claim, dict) else []
            require(bool(re.fullmatch(r"[a-z0-9-]+", claim_id)), f"{branch_file} : identifiant d'affirmation invalide")
            require(claim_id not in claim_ids, f"{branch_file} : affirmation dupliquée {claim_id}")
            claim_ids.add(claim_id)
            require(bool(statement), f"{branch_file}/{claim_id} : formulation manquante")
            require(status == "verified", f"{branch_file}/{claim_id} : affirmation importante non vérifiée")
            require(not UNVERIFIED_TERMS.search(statement), f"{branch_file}/{claim_id} : formulation contient une réserve bloquante")
            require(isinstance(source_ids, list) and bool(source_ids), f"{branch_file}/{claim_id} : identifiant de source manquant")
            for source_id in source_ids if isinstance(source_ids, list) else []:
                require(source_id in registry_sources, f"{branch_file}/{claim_id} : source absente ou sans URL officielle {source_id}")
                if source_id in registry_sources:
                    host = urlparse(registry_sources[source_id]).hostname
                    require(host in OFFICIAL_HOSTS, f"{branch_file}/{claim_id} : domaine non officiel pour {source_id}")
                    require(f"`{source_id}`" in branch_content, f"{branch_file}/{claim_id} : source {source_id} non citée dans la branche")

instances = (ROOT / "references" / "instances-dialogue-social.md").read_text(encoding="utf-8")
deontology = (ROOT / "references" / "deontologie-conflits-interets.md").read_text(encoding="utf-8")
require("2025-1430" in instances, "Instances : décret n° 2025-1430 non référencé")
require("ne constitue pas un délai légal automatique" in deontology, "Déontologie : réserve interne / délai légal non distingués")
require("emplois mentionnés à l'article L. 124-5" in deontology, "Déontologie : champ de L. 124-7 insuffisamment borné")
require("3 fiabilisées, 4" in skill, "SKILL.md : bilan de maturité v0.7.0 incohérent")

if errors:
    print("ÉCHEC")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK — structure, renvois et garde-fous vérifiés.")
