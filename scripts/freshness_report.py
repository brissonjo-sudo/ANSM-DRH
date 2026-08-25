"""Rapport préventif sur l'expiration prochaine des sources."""

from __future__ import annotations

from argparse import ArgumentParser
from datetime import date, timedelta
import json
from pathlib import Path
import sys


def build_report(manifest: object, today: date, warning_days: int = 7) -> dict:
    if not isinstance(manifest, dict) or not isinstance(manifest.get("branches"), dict):
        raise ValueError("Manifeste de sources invalide")
    items: list[dict] = []
    for branch, gate in manifest["branches"].items():
        if not isinstance(gate, dict):
            raise ValueError(f"Configuration invalide pour {branch}")
        for claim in gate.get("claims", []):
            try:
                checked_on = date.fromisoformat(claim["checked_on"])
                max_age_days = int(claim["max_age_days"])
                claim_id = claim["id"]
            except (KeyError, TypeError, ValueError) as exc:
                raise ValueError(f"Affirmation invalide dans {branch}") from exc
            deadline = checked_on + timedelta(days=max_age_days)
            remaining = (deadline - today).days
            if remaining <= warning_days:
                items.append({
                    "branch": branch,
                    "claim_id": claim_id,
                    "checked_on": checked_on.isoformat(),
                    "deadline": deadline.isoformat(),
                    "days_remaining": remaining,
                    "state": "expired" if remaining < 0 else "warning",
                })
    items.sort(key=lambda item: (item["days_remaining"], item["branch"], item["claim_id"]))
    state = "expired" if any(item["state"] == "expired" for item in items) else "warning" if items else "ok"
    return {
        "generated_on": today.isoformat(),
        "warning_days": warning_days,
        "state": state,
        "items": items,
    }


def render_markdown(report: dict) -> str:
    labels = {"ok": "À jour", "warning": "À renouveler", "expired": "Expirée"}
    lines = [
        "# Suivi de fraîcheur des sources",
        "",
        f"État : **{labels[report['state']]}** — rapport du {report['generated_on']}.",
        "",
    ]
    if not report["items"]:
        lines.append(f"Aucune source n'expire dans les {report['warning_days']} prochains jours.")
        return "\n".join(lines) + "\n"
    lines.extend([
        "| État | Branche | Affirmation | Échéance | Jours restants |",
        "|---|---|---|---|---:|",
    ])
    for item in report["items"]:
        label = "expirée" if item["state"] == "expired" else "à renouveler"
        lines.append(
            f"| {label} | `{item['branch']}` | `{item['claim_id']}` | "
            f"{item['deadline']} | {item['days_remaining']} |"
        )
    lines.extend([
        "",
        "Action : revoir la source officielle, puis mettre à jour `checked_on` "
        "et la date de vérification de la branche.",
    ])
    return "\n".join(lines) + "\n"


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    parser = ArgumentParser(description="Prépare les alertes d'expiration des sources.")
    parser.add_argument("--manifest", type=Path, default=root / "evals" / "source-gates.json")
    parser.add_argument("--today", type=date.fromisoformat, default=date.today())
    parser.add_argument("--warning-days", type=int, default=7)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--markdown-output", type=Path)
    args = parser.parse_args()
    if args.warning_days < 0:
        parser.error("--warning-days doit être positif")
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        report = build_report(manifest, args.today, args.warning_days)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ÉCHEC — {exc}")
        return 1
    rendered_json = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    rendered_markdown = render_markdown(report)
    if args.json_output:
        args.json_output.write_text(rendered_json, encoding="utf-8")
    if args.markdown_output:
        args.markdown_output.write_text(rendered_markdown, encoding="utf-8")
    if not args.json_output and not args.markdown_output:
        print(rendered_markdown, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
