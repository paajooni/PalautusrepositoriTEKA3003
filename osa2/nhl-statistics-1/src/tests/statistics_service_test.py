import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self, name="Kurri"):
        player = self.stats.search(name)
        self.assertEqual(player.name, "Kurri")

    def test_team(self, team_name="EDM"):
        team_players = self.stats.team(team_name)
        self.assertEqual(len(team_players), 3)

    def test_top(self, how_many=3):
        top_players = self.stats.top(how_many)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_search_returns_none_for_unknown_player(self):
        player = self.stats.search("Unknown")
        self.assertIsNone(player)

    def test_team_returns_empty_list_for_unknown_team(self):
        team_players = self.stats.team("...")
        self.assertEqual(team_players, [])
