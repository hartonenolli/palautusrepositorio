import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_by_name(self):
        haetaan = self.statistics.search("Semenko")
        self.assertEqual(haetaan.name, "Semenko")

    def test_find_player_team(self):
        haetaan = self.statistics.team("EDM")
        self.assertEqual(haetaan[1].name, "Kurri")

    def test_find_player_wrong_name(self):
        haetaan = self.statistics.search("Hartonen")
        self.assertEqual(haetaan, None)
    
    def test_top(self):
        haetaan = self.statistics.top(4)
        top4 = [haetaan[0].name, haetaan[1].name, haetaan[2].name,
            haetaan[3].name
            ]
        self.assertEqual(top4, ["Gretzky", "Lemieux", "Yzerman", "Kurri"])
    
    def test_parhausperuste_1(self):
        haetaan = self.statistics.top(4, 1)
        top4 = [haetaan[0].name, haetaan[1].name, haetaan[2].name,
            haetaan[3].name
            ]
        self.assertEqual(top4, ["Gretzky", "Lemieux", "Yzerman", "Kurri"])

    def test_parhausperuste_2(self):
        haetaan = self.statistics.top(4, 2)
        top4 = [haetaan[0].name, haetaan[1].name, haetaan[2].name,
            haetaan[3].name
            ]
        self.assertEqual(top4, ["Lemieux", "Yzerman", "Kurri", "Gretzky"])
    
    def test_parhausperuste_3(self):
        haetaan = self.statistics.top(4, 3)
        top4 = [haetaan[0].name, haetaan[1].name, haetaan[2].name,
            haetaan[3].name
            ]
        self.assertEqual(top4, ["Gretzky", "Yzerman", "Lemieux", "Kurri"])
