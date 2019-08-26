import unittest
from deck import Deck


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_class_attributes(self):
        """Deck begins with 52 cards"""
        self.assertEqual(len(Deck.cards), 52)

    def test_instance_method_count(self):
        """count method returns the number of cards in the deck"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_instance_method_shuffle(self):
        """shuffle method returns a reordered deck of the same length"""
        old_cards = self.deck.cards.copy()
        self.deck.shuffle()
        new_cards = self.deck.cards
        self.assertEqual(len(old_cards), len(new_cards))
        self.assertNotEqual(old_cards, new_cards)

    def test_instance_method_deal_card(self):
        """deal_card removes the first card from the deck and returns it"""
        first_card = self.deck.cards[0]
        self.assertEqual(self.deck.deal_card(), first_card)
        self.assertEqual(len(self.deck.cards), 51)

    def test_instance_method_deal_hand(self):
        """deal_hand removes the provided number of cards from the deck and returns them"""
        hand_size = 5
        hand = self.deck.cards[0:hand_size]
        self.assertEqual(self.deck.deal_hand(hand_size), hand)
        self.assertEqual(len(self.deck.cards), 47)


if __name__ == "__main__":
    unittest.main()
