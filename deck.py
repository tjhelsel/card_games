from card import Card
from random import shuffle


class Deck:
    cards = tuple((Card(suit, val)
                   for suit in Card.suits for val in Card.values))

    def __init__(self):
        self.cards = list(Deck.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, qty):
        remaining = self.count()
        if remaining == 0:
            raise ValueError('All cards have been dealt')
        elif remaining < qty:
            qty = remaining
            print(f"Only {qty} cards remaining in deck; dealing {qty} cards.")
        cards_dealt = self.cards[0:qty]
        del self.cards[0:qty]
        return cards_dealt

    def shuffle(self):
        if self.count() != 52:
            raise ValueError('Only full decks can be shuffled')
        shuffle(self.cards)
        return self.cards

    def deal_card(self):
        dealt_cards = self._deal(1)
        return dealt_cards[0]

    def deal_hand(self, qty):
        dealt_cards = self._deal(qty)
        return dealt_cards


my_deck = Deck()

for card in my_deck:
    print(card)
