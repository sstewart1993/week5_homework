import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Hearts", 10)
        self.card2 = Card("Hearts", 1)
        self.card_game = CardGame()


    def test_check_for_ace(self):
        self.assertEqual(1, self.card2.value)

    def test_highest_card(self):
        self.assertEqual(10, self.card1.value)
        
    def test_cards_total(self):
        cards = [self.card1, self.card2]
        total = self.card_game.cards_total(cards)
        self.assertEquals("You have a total of 11", total)
