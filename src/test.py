import unittest
from unittest.mock import patch
from card import Card
from player import Player
from main import MainWindow


class TestCard(unittest.TestCase):

    def test_val(self):
        card = Card("d", 2)
        self.assertEqual(card.get_val(), 2)

    def test_suit(self):
        card = Card("d", 2)
        self.assertEqual(card.get_suit(), "d")

    def test_val_incorrect(self):
        card = Card("d", 2)
        self.assertNotEqual(card.get_val(), 5)

    def test_count_points(self):
        player = Player("test")
        cards = [Card("d", 1), Card("s", 1), Card("d", 5), Card("d", 10)]
        player.cards = cards
        player.mokki = 2
        player.count_points()
        self.assertEqual(player.points, 6)


if __name__ == '__main__':
    unittest.main()
