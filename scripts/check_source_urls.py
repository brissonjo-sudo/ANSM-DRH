"""Vérifie en parallèle l'accessibilité des URL du registre de sources."""

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "references" / "sources-principales.md"
SOURCE_PATTERN = re.compile(r"^\| `([^`]+)` \|.*?\| <(https://[^>]+)> \|", re.MULTILINE)
USER_AGENT = "ANSM-DRH-source-check/0.7 (+https://github.com/brissonjo-sudo/ANSM-DRH)"


def check_url(source_id: str, url: str) -> tuple[str, str, int | None, str | None]:
    """Retourne l'identifiant, l'URL, le statut HTTP et une erreur éventuelle."""
    last_error: str | None = None
    for method in ("HEAD", "GET"):
        request = Request(url, headers={"User-Agent": USER_AGENT}, method=method)
        try:
            with urlopen(request, timeout=20) as response:
                status = response.getcode()
                if 200 <= status < 400:
                    return source_id, url, status, None
                last_error = f"HTTP {status}"
        except HTTPError as exc:
            last_error = f"HTTP {exc.code}"
            host = urlparse(url).hostname
            if exc.code == 403 and host == "www.legifrance.gouv.fr":
                return source_id, url, 403, None
            if exc.code != 405:
                break
        except (URLError, TimeoutError, OSError) as exc:
            last_error = str(exc)
    return source_id, url, None, last_error or "erreur inconnue"


def main() -> int:
    sources = SOURCE_PATTERN.findall(REGISTRY.read_text(encoding="utf-8"))
    if not sources:
        print("ÉCHEC — aucune URL trouvée dans le registre")
        return 1

    failures: list[tuple[str, str, str]] = []
    with ThreadPoolExecutor(max_workers=min(8, len(sources))) as executor:
        futures = {executor.submit(check_url, source_id, url): source_id for source_id, url in sources}
        for future in as_completed(futures):
            source_id, url, status, error = future.result()
            if error:
                failures.append((source_id, url, error))
            else:
                suffix = " (protection anti-robot Légifrance)" if status == 403 else ""
                print(f"OK {source_id} — HTTP {status}{suffix}")

    if failures:
        print("ÉCHEC — URL officielles inaccessibles")
        for source_id, url, error in sorted(failures):
            print(f"- {source_id}: {error} — {url}")
        return 1

    print(f"OK — {len(sources)} URL officielles répondent ou sont protégées par Légifrance")
    return 0


if __name__ == "__main__":
    sys.exit(main())
