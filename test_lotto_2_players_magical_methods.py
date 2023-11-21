import unittest
from lotto_2_players_magical_methods import Card, Game


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card1 = Card(list(range(1, 91)))
        self.card2 = Card(list(range(1, 91)))

    def test_str(self):
        self.assertIsInstance(str(self.card1), str)

    def test_eq(self):
        self.assertNotEqual(self.card1, self.card2)


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game1 = Game()
        self.game2 = Game()

    def test_str(self):
        self.assertIsInstance(str(self.game1), str)

    def test_eq(self):
        self.assertNotEqual(self.game1, self.game2)

    def test_draw_number(self):
        drawn_number = self.game1.draw_number()
        self.assertIn(drawn_number, list(range(1, 91)))
        self.assertNotIn(drawn_number, self.game1.remaining_numbers)

    def test_check_winner(self):
        self.assertFalse(self.game1.check_winner(self.game1.player_card))
        self.assertFalse(self.game1.check_winner(self.game1.computer_card))


if __name__ == '__main__':
    unittest.main()
