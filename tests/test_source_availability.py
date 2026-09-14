"""Tests du partage entre URL morte et hôte indisponible.

Une panne chez une source officielle ne doit pas bloquer les fusions du dépôt ;
une URL réellement morte, si.
"""

import unittest

from scripts.check_source_urls import classify_failure, summarize


OK_LEGIFRANCE = ("CGFP-LIVRE4", "https://www.legifrance.gouv.fr/x", 403, None)
OK_DGAFP = ("DGAFP-ELECTIONS-2026", "https://www.fonction-publique.gouv.fr/y", 200, None)


def failure(source_id: str, error: str):
    return (source_id, f"https://ansm.sante.fr/{source_id}.pdf", None, error)


class ClassifyFailureTests(unittest.TestCase):
    def test_not_found_is_dead(self) -> None:
        self.assertEqual("dead", classify_failure("HTTP 404"))
        self.assertEqual("dead", classify_failure("HTTP 410"))

    def test_server_errors_are_unavailable(self) -> None:
        for status in ("HTTP 500", "HTTP 502", "HTTP 503", "HTTP 504"):
            self.assertEqual("unavailable", classify_failure(status), status)

    def test_rate_limit_and_timeouts_are_unavailable(self) -> None:
        self.assertEqual("unavailable", classify_failure("HTTP 429"))
        self.assertEqual("unavailable", classify_failure("HTTP 408"))

    def test_transport_errors_are_unavailable(self) -> None:
        # Les messages réels produits par check_url lors de la panne ANSM du
        # 13 septembre 2026.
        self.assertEqual(
            "unavailable", classify_failure("<urlopen error [Errno 104] Connection reset by peer>")
        )
        self.assertEqual("unavailable", classify_failure("<urlopen error timed out>"))
        self.assertEqual("unavailable", classify_failure("erreur inconnue"))

    def test_unexpected_client_errors_stay_blocking(self) -> None:
        # Un 401 ou un 451 peut signaler que la ressource a changé d'accès :
        # par prudence, on ne les range pas parmi les pannes passagères.
        self.assertEqual("dead", classify_failure("HTTP 401"))
        self.assertEqual("dead", classify_failure("HTTP 451"))


class SummarizeTests(unittest.TestCase):
    def test_all_reachable_passes(self) -> None:
        exit_code, lines = summarize([OK_LEGIFRANCE, OK_DGAFP])
        self.assertEqual(0, exit_code)
        self.assertIn("OK — 2 URL officielles sur 2", lines[-1])

    def test_host_outage_warns_without_blocking(self) -> None:
        exit_code, lines = summarize(
            [OK_LEGIFRANCE, OK_DGAFP, failure("ANSM-DEONTO-2025", "HTTP 502")]
        )
        self.assertEqual(0, exit_code)
        report = "\n".join(lines)
        self.assertIn("AVERTISSEMENT", report)
        self.assertIn("ANSM-DEONTO-2025", report)
        self.assertNotIn("ÉCHEC", report)

    def test_dead_url_blocks(self) -> None:
        exit_code, lines = summarize(
            [OK_LEGIFRANCE, OK_DGAFP, failure("ANSM-DEONTO-2025", "HTTP 404")]
        )
        self.assertEqual(1, exit_code)
        self.assertIn("ÉCHEC", "\n".join(lines))

    def test_dead_url_blocks_even_alongside_an_outage(self) -> None:
        # Une panne concomitante ne doit pas masquer une URL réellement morte.
        exit_code, lines = summarize(
            [
                OK_DGAFP,
                failure("ANSM-DEONTO-2025", "HTTP 502"),
                failure("ANSM-CHARTE-2026", "HTTP 404"),
            ]
        )
        self.assertEqual(1, exit_code)
        report = "\n".join(lines)
        self.assertIn("AVERTISSEMENT", report)
        self.assertIn("ÉCHEC", report)

    def test_total_outage_blocks(self) -> None:
        # Si rien ne répond, c'est le contrôle qui est aveugle : le laisser
        # passer reviendrait à valider sans avoir rien vérifié.
        exit_code, lines = summarize(
            [
                failure("ANSM-DEONTO-2025", "HTTP 502"),
                failure("ANSM-CHARTE-2026", "<urlopen error timed out>"),
            ]
        )
        self.assertEqual(1, exit_code)
        self.assertIn("pas d'accès réseau", "\n".join(lines))

    def test_report_order_is_deterministic(self) -> None:
        # Le rapport ne doit pas dépendre de l'ordre d'arrivée des réponses.
        forward = summarize([OK_LEGIFRANCE, OK_DGAFP])[1]
        backward = summarize([OK_DGAFP, OK_LEGIFRANCE])[1]
        self.assertEqual(forward, backward)


if __name__ == "__main__":
    unittest.main()
