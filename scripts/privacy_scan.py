"""Détection locale de données RH directement identifiantes."""

from __future__ import annotations

from argparse import ArgumentParser
import json
from pathlib import Path
import re
import sys


IDENTIFIER_PATTERNS = {
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "telephone": re.compile(r"(?<!\d)(?:\+33|0)[1-9](?:[ .-]?\d{2}){4}(?!\d)"),
    "iban": re.compile(r"\bFR\d{2}(?:[ -]?[0-9A-Z]){23}\b", re.IGNORECASE),
    "nir": re.compile(r"(?<!\d)[12][ -]?\d{2}[ -]?(?:0[1-9]|1[0-2])[ -]?(?:2[AB]|\d{2})[ -]?\d{3}[ -]?\d{3}[ -]?\d{2}(?!\d)", re.IGNORECASE),
    "matricule": re.compile(r"\bmatricule\s*(?:n[°o]\s*)?[:#-]?\s*[A-Z0-9-]{4,}\b", re.IGNORECASE),
}
SENSITIVE_CONTEXT = {
    "health": re.compile(r"\b(santé|maladie|handicap|médical|médecin|arrêt de travail|rps|souffrance)\b", re.IGNORECASE),
    "disciplinary": re.compile(r"\b(disciplinaire|sanction|faute|harcèlement|signalement|enquête interne)\b", re.IGNORECASE),
}
REPLACEMENTS = {
    "email": "[COURRIEL SUPPRIMÉ]",
    "telephone": "[TÉLÉPHONE SUPPRIMÉ]",
    "iban": "[IBAN SUPPRIMÉ]",
    "nir": "[NIR SUPPRIMÉ]",
    "matricule": "[MATRICULE SUPPRIMÉ]",
}


def scan_text(content: str) -> list[dict]:
    """Retourne les catégories et positions, jamais la valeur détectée."""
    findings: list[dict] = []
    for kind, pattern in IDENTIFIER_PATTERNS.items():
        for match in pattern.finditer(content):
            findings.append({
                "kind": kind,
                "severity": "high" if kind in {"nir", "iban"} else "medium",
                "start": match.start(),
                "end": match.end(),
            })
    for kind, pattern in SENSITIVE_CONTEXT.items():
        if pattern.search(content):
            findings.append({"kind": f"sensitive_{kind}", "severity": "warning"})
    if any(item["kind"].startswith("sensitive_") for item in findings) and any(
        item["kind"] in IDENTIFIER_PATTERNS for item in findings
    ):
        findings.append({"kind": "identified_sensitive_case", "severity": "high"})
    return findings


def redact_text(content: str) -> str:
    """Pseudonymise les identifiants structurés détectables."""
    redacted = content
    for kind, pattern in IDENTIFIER_PATTERNS.items():
        redacted = pattern.sub(REPLACEMENTS[kind], redacted)
    return redacted


def main() -> int:
    parser = ArgumentParser(description="Repère les données RH à pseudonymiser.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--redact", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    content = args.input.read_text(encoding="utf-8")
    findings = scan_text(content)
    if args.redact:
        rendered = redact_text(content)
    else:
        rendered = json.dumps({"findings": findings}, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 2 if any(item["severity"] == "high" for item in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
