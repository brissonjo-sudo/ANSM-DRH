"""Contrôles légers, sans dépendance, pour la publication du skill."""

from pathlib import Path
from datetime import date
import argparse
import json
import re
import sys

from source_gate import BRANCH_FILES, parse_registry, validate_source_gates
from behavior_eval import validate_suite
from internal_sources import validate_requirements


parser = argparse.ArgumentParser(description="Valide la structure et les sources du skill.")
parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
parser.add_argument("--today", type=date.fromisoformat, default=date.today())
args = parser.parse_args()

ROOT = args.root.resolve()
TODAY = args.today
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
    registry_sources = parse_registry(registry_content)

source_gates_path = ROOT / "evals" / "source-gates.json"
require(source_gates_path.is_file(), "Barrière de fiabilisation evals/source-gates.json manquante")
if source_gates_path.is_file():
    try:
        source_gates = json.loads(source_gates_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f"Barrière de fiabilisation illisible : {exc}")
        source_gates = {"branches": {}}

    branch_contents = {
        branch_file: (ROOT / branch_file).read_text(encoding="utf-8")
        for branch_file in BRANCH_FILES
        if (ROOT / branch_file).is_file()
    }
    errors.extend(validate_source_gates(source_gates, registry_sources, branch_contents, TODAY))

behavior_path = ROOT / "evals" / "behavior-cases.json"
require(behavior_path.is_file(), "Suite comportementale evals/behavior-cases.json manquante")
if behavior_path.is_file():
    try:
        behavior_suite = json.loads(behavior_path.read_text(encoding="utf-8"))
        errors.extend(validate_suite(behavior_suite))
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f"Suite comportementale illisible : {exc}")

internal_sources_path = ROOT / "evals" / "internal-source-requirements.json"
require(internal_sources_path.is_file(), "Registre des besoins internes manquant")
if internal_sources_path.is_file():
    try:
        internal_sources = json.loads(internal_sources_path.read_text(encoding="utf-8"))
        errors.extend(validate_requirements(internal_sources))
    except (json.JSONDecodeError, OSError) as exc:
        errors.append(f"Registre des besoins internes illisible : {exc}")

instances = (ROOT / "references" / "instances-dialogue-social.md").read_text(encoding="utf-8")
deontology = (ROOT / "references" / "deontologie-conflits-interets.md").read_text(encoding="utf-8")
require("2025-1430" in instances, "Instances : décret n° 2025-1430 non référencé")
require("ne constitue pas un délai légal automatique" in deontology, "Déontologie : réserve interne / délai légal non distingués")
require("emplois mentionnés à l'article L. 124-5" in deontology, "Déontologie : champ de L. 124-7 insuffisamment borné")
require("3 fiabilisées, 4" in skill, "SKILL.md : bilan de maturité v0.9.4 incohérent")
require("version: 0.9.4" in skill, "SKILL.md : version 0.9.4 attendue")

if errors:
    print("ÉCHEC")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK — structure, renvois et garde-fous vérifiés.")
