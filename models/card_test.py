import unittest
from card import Card


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('hearts', '2')
        self.card2 = Card('spades', 'K')

    def test_class_attributes(self):
        """Card class has 4 suits and 13 values"""
        self.assertEqual(len(Card.suits), 4)
        self.assertEqual(len(Card.values), 13)

    def test_instance_attributes_suit(self):
        """Card instance has suit assigned on instantiation"""
        self.assertEqual(self.card1.suit, 'hearts')
        self.assertEqual(self.card2.suit, 'spades')

    def test_instance_attributes_value(self):
        """Card instance has value assigned on instantiation"""
        self.assertEqual(self.card1.value, '2')
        self.assertEqual(self.card2.value, 'K')


if __name__ == "__main__":
    unittest.main()
