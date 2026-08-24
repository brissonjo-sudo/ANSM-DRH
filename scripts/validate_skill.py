"""Contrôles légers, sans dépendance, pour la publication du skill."""

from pathlib import Path
import re
import sys


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
require(registry.is_file(), "Registre des sources principales manquant")
if registry.is_file():
    registry_content = registry.read_text(encoding="utf-8")
    require("https://" in registry_content, "Registre des sources sans lien officiel")
    require("CGFP-ENTRANT" in registry_content, "Registre : contrôle déontologique entrant manquant")
    require("LFSS-DOTATION-2026" in registry_content, "Registre : source légale de la dotation 2026 manquante")
    require("ANSM-DEONTO-2023" in registry_content, "Registre : rapport public ANSM 2023 manquant")

instances = (ROOT / "references" / "instances-dialogue-social.md").read_text(encoding="utf-8")
deontology = (ROOT / "references" / "deontologie-conflits-interets.md").read_text(encoding="utf-8")
require("2025-1430" in instances, "Instances : décret n° 2025-1430 non référencé")
require("ne constitue pas un délai légal automatique" in deontology, "Déontologie : réserve interne / délai légal non distingués")
require("emplois mentionnés à l'article L. 124-5" in deontology, "Déontologie : champ de L. 124-7 insuffisamment borné")
require("3 fiabilisées, 4" in skill, "SKILL.md : bilan de maturité v0.6.1 incohérent")

if errors:
    print("ÉCHEC")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("OK — structure, renvois et garde-fous vérifiés.")
