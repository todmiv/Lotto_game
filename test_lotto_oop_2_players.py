import unittest
from io import StringIO
import sys
from lotto_oop_2_players import Card, Game


class TestCard(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_init(self):
        card = Card()
        self.assertEqual(len(card.rows), 3)
        self.assertEqual(len(card.digits), 75)

    def test_print_card(self):
        card = Card()

        captured_output = StringIO()
        sys.stdout = captured_output

        card.print_card()

        printed_output = captured_output.getvalue().strip()
        print("printed_output", printed_output)

        expected_output = "--------------------------"
        for row in card.rows:
            expected_output += "\n"
            for num in row:
                if num == 0:
                    expected_output += "-  "
                else:
                    expected_output += f"{num:2d} "

        expected_output += "\n--------------------------"
        print("expected_output", expected_output)

        self.assertEqual(printed_output, expected_output)

    def test_print_card_format(self):
        card = Card()
        output = card.print_card_format()
        self.assertEqual(output, None)


class TestGame(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.game = None

    def test_init(self):
        game = Game()
        self.assertIsInstance(game.player_card, Card)
        self.assertIsInstance(game.computer_card, Card)
        self.assertEqual(len(game.remaining_numbers), 90)

    def test_draw_number(self):
        game = Game()
        number = game.draw_number()
        self.assertFalse(number in game.remaining_numbers)

    def test_check_winner(self):
        card = Card()
        card.rows = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        game = Game()
        self.assertTrue(game.check_winner(card))

    #def test_play(self):
        #game = Game()
        #game.play()
