"""Tests de la reprise sur coupure réseau du contrôle d'URL."""

from urllib.error import HTTPError, URLError
from urllib.request import Request
import unittest

from scripts.check_source_urls import check_url, summarize


LEGIFRANCE = "https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006690378"
RESET = URLError(ConnectionResetError(104, "Connection reset by peer"))


class FakeResponse:
    """Réponse minimale : un statut et un gestionnaire de contexte."""

    def __init__(self, status: int) -> None:
        self.status = status

    def getcode(self) -> int:
        return self.status

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *exc_info) -> bool:
        return False


class FakeOpener:
    """Rejoue une liste de resultats scriptes et note les methodes appelees."""

    def __init__(self, outcomes: list) -> None:
        self.outcomes = list(outcomes)
        self.methods: list[str] = []

    def __call__(self, request: Request, timeout: int | None = None) -> FakeResponse:
        self.methods.append(request.get_method())
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return FakeResponse(outcome)


def http_error(code: int, url: str = "https://example.org/x") -> HTTPError:
    return HTTPError(url, code, f"erreur {code}", {}, None)


class CheckSourceUrlsRetryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.delays: list[float] = []

    def run_check(self, outcomes: list, url: str = "https://example.org/x", **kwargs):
        opener = FakeOpener(outcomes)
        result = check_url(
            "SOURCE-ID", url, sleep=self.delays.append, opener=opener, **kwargs
        )
        return result, opener

    def test_reprend_apres_une_coupure_reseau(self) -> None:
        # HEAD et GET coupent, puis le HEAD de la 2e tentative répond.
        (_, _, status, error), opener = self.run_check([RESET, RESET, 200])
        self.assertEqual(200, status)
        self.assertIsNone(error)
        self.assertEqual(1, len(self.delays))
        self.assertEqual(["HEAD", "GET", "HEAD"], opener.methods)

    def test_attente_double_entre_les_tentatives(self) -> None:
        self.run_check([RESET] * 4)
        self.assertEqual([1.5], self.delays)

    def test_abandon_apres_le_nombre_de_tentatives(self) -> None:
        (_, _, status, error), opener = self.run_check([RESET] * 4)
        self.assertIsNone(status)
        self.assertIn("Connection reset by peer", error)
        self.assertEqual(4, len(opener.methods))

    def test_echec_persistant_devient_avertissement_non_bloquant(self) -> None:
        result, _ = self.run_check([RESET] * 4)
        exit_code, lines = summarize([
            ("OK", "https://example.org/ok", 200, None),
            result,
        ])
        self.assertEqual(0, exit_code)
        self.assertIn("AVERTISSEMENT", "\\n".join(lines))

    def test_indisponibilite_totale_reste_bloquante(self) -> None:
        result, _ = self.run_check([RESET] * 4)
        exit_code, lines = summarize([result])
        self.assertEqual(1, exit_code)
        self.assertIn("aucune URL", "\\n".join(lines))

    def test_une_url_morte_echoue_sans_reprise(self) -> None:
        (_, _, status, error), opener = self.run_check([http_error(404)])
        self.assertIsNone(status)
        self.assertEqual("HTTP 404", error)
        self.assertEqual([], self.delays)
        self.assertEqual(["HEAD"], opener.methods)

    def test_le_serveur_surcharge_est_retente(self) -> None:
        (_, _, status, error), _ = self.run_check([http_error(429), 200])
        self.assertEqual(200, status)
        self.assertIsNone(error)
        self.assertEqual(1, len(self.delays))

    def test_erreur_serveur_est_retentee(self) -> None:
        (_, _, status, _), _ = self.run_check([http_error(503), 200])
        self.assertEqual(200, status)
        self.assertEqual(1, len(self.delays))

    def test_403_legifrance_reste_un_succes(self) -> None:
        (_, _, status, error), _ = self.run_check([http_error(403, LEGIFRANCE)], url=LEGIFRANCE)
        self.assertEqual(403, status)
        self.assertIsNone(error)
        self.assertEqual([], self.delays)

    def test_403_hors_legifrance_reste_un_echec(self) -> None:
        (_, _, status, error), _ = self.run_check([http_error(403)])
        self.assertIsNone(status)
        self.assertEqual("HTTP 403", error)
        self.assertEqual([], self.delays)

    def test_head_refuse_bascule_sur_get(self) -> None:
        (_, _, status, _), opener = self.run_check([http_error(405), 200])
        self.assertEqual(200, status)
        self.assertEqual(["HEAD", "GET"], opener.methods)
        self.assertEqual([], self.delays)


if __name__ == "__main__":
    unittest.main()
