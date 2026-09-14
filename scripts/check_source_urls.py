"""Vérifie en parallèle l'accessibilité des URL du registre de sources."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import re
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "references" / "sources-principales.md"
SOURCE_PATTERN = re.compile(r"^\| `([^`]+)` \|.*?\| <(https://[^>]+)> \|", re.MULTILINE)
USER_AGENT = "ANSM-DRH-source-check/0.8 (+https://github.com/brissonjo-sudo/ANSM-DRH)"

# Deux familles d'échec, qui ne disent pas la même chose et n'appellent pas la
# même sanction.
#
# Une URL **morte** (404, 410) est un défaut du registre : la pièce a été
# déplacée ou retirée, une branche cite une source qui n'existe plus, et cela
# doit bloquer la fusion.
#
# Un **hôte indisponible** (coupure réseau, délai dépassé, 429, 5xx) ne dit
# rien de la validité de l'URL. Faire échouer le dépôt entier parce qu'un site
# officiel est en panne revient à suspendre tout travail le temps qu'un tiers
# se rétablisse — pour une information qui ne concerne pas le contenu versionné.
# Ces cas sont signalés, pas bloquants.
DEAD_STATUSES = frozenset({404, 410})
UNAVAILABLE_STATUSES = frozenset({408, 425, 429})
HTTP_ERROR = re.compile(r"^HTTP (\d{3})$")


def classify_failure(error: str) -> str:
    """« dead » si l'URL est morte, « unavailable » si c'est l'hôte qui flanche."""
    match = HTTP_ERROR.match(error.strip())
    if match is None:
        # Erreur de transport : coupure, délai dépassé, résolution DNS. Rien
        # à conclure sur l'URL elle-même.
        return "unavailable"
    status = int(match.group(1))
    if status in DEAD_STATUSES:
        return "dead"
    if status in UNAVAILABLE_STATUSES or status >= 500:
        return "unavailable"
    # Tout autre code (401, 403 hors Légifrance, 451…) peut signaler un
    # changement d'accès à la ressource : on reste bloquant par prudence.
    return "dead"


# Les erreurs brèves sont retentées avant d'être classées par summarize().
# Deux tentatives suffisent à absorber un incident ponctuel sans prolonger
# fortement la CI lorsque l'hôte reste indisponible.
RETRY_ATTEMPTS = 2
RETRY_BACKOFF = 1.5


def _attempt(url: str, opener) -> tuple[int | None, str | None, bool]:
    """Tente HEAD puis GET. Retourne (statut, erreur, erreur transitoire)."""
    last_error: str | None = None
    transient = False
    for method in ("HEAD", "GET"):
        request = Request(url, headers={"User-Agent": USER_AGENT}, method=method)
        try:
            with opener(request, timeout=20) as response:
                status = response.getcode()
                if 200 <= status < 400:
                    return status, None, False
                last_error = f"HTTP {status}"
                transient = status in UNAVAILABLE_STATUSES or status >= 500
        except HTTPError as exc:
            last_error = f"HTTP {exc.code}"
            host = urlparse(url).hostname
            if exc.code == 403 and host == "www.legifrance.gouv.fr":
                return 403, None, False
            transient = exc.code in UNAVAILABLE_STATUSES or exc.code >= 500
            if exc.code != 405:
                break
        except (URLError, TimeoutError, OSError) as exc:
            last_error = str(exc)
            transient = True
    return None, last_error, transient


def check_url(
    source_id: str,
    url: str,
    *,
    attempts: int = RETRY_ATTEMPTS,
    sleep=time.sleep,
    opener=urlopen,
) -> tuple[str, str, int | None, str | None]:
    """Vérifie une URL et retente uniquement les échecs transitoires."""
    last_error: str | None = None
    for attempt in range(1, attempts + 1):
        status, last_error, transient = _attempt(url, opener)
        if status is not None:
            return source_id, url, status, None
        if not transient or attempt == attempts:
            break
        sleep(RETRY_BACKOFF * 2 ** (attempt - 1))
    return source_id, url, None, last_error or "erreur inconnue"
def summarize(
    results: list[tuple[str, str, int | None, str | None]],
) -> tuple[int, list[str]]:
    """Trie les résultats et décide du code de sortie.

    Séparé de la collecte réseau pour rester testable, et pour que l'ordre du
    rapport ne dépende pas de l'ordre d'arrivée des réponses.
    """
    reachable: list[str] = []
    dead: list[tuple[str, str, str]] = []
    unavailable: list[tuple[str, str, str]] = []

    for source_id, url, status, error in results:
        if error:
            bucket = dead if classify_failure(error) == "dead" else unavailable
            bucket.append((source_id, url, error))
        else:
            suffix = " (protection anti-robot Légifrance)" if status == 403 else ""
            reachable.append(f"OK {source_id} — HTTP {status}{suffix}")

    lines = sorted(reachable)

    if unavailable:
        lines.append("AVERTISSEMENT — hôtes momentanément indisponibles (non bloquant)")
        for source_id, url, error in sorted(unavailable):
            lines.append(f"- {source_id}: {error} — {url}")
        lines.append(
            "  Ces URL ne sont pas réputées mortes : l'hôte n'a pas répondu. "
            "Les recontrôler une fois le service rétabli."
        )

    if dead:
        lines.append("ÉCHEC — URL officielles mortes ou devenues inaccessibles")
        for source_id, url, error in sorted(dead):
            lines.append(f"- {source_id}: {error} — {url}")
        return 1, lines

    if unavailable and not reachable:
        # Aucune source n'a répondu : ce n'est plus la panne d'un tiers, c'est
        # le contrôle lui-même qui n'a pas d'accès réseau. Le laisser passer
        # reviendrait à valider sans rien avoir vérifié.
        lines.append(
            "ÉCHEC — aucune URL n'a répondu : le contrôle n'a pas d'accès réseau"
        )
        return 1, lines

    lines.append(
        f"OK — {len(reachable)} URL officielles sur {len(results)} répondent "
        "ou sont protégées par Légifrance"
    )
    return 0, lines


def main() -> int:
    sources = SOURCE_PATTERN.findall(REGISTRY.read_text(encoding="utf-8"))
    if not sources:
        print("ÉCHEC — aucune URL trouvée dans le registre")
        return 1

    results: list[tuple[str, str, int | None, str | None]] = []
    with ThreadPoolExecutor(max_workers=min(8, len(sources))) as executor:
        futures = {executor.submit(check_url, source_id, url): source_id for source_id, url in sources}
        for future in as_completed(futures):
            results.append(future.result())

    exit_code, lines = summarize(results)
    for line in lines:
        print(line)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
