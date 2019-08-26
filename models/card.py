class Card:
    suits = ('hearts', 'diamonds', 'clubs', 'spades')
    number_cards = tuple(str(n) for n in range(2, 11))
    face_cards = ('J', 'Q', 'K')
    ace_card = ('A',)
    values = number_cards + face_cards + ace_card

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def __init__(self, suit, value):
        if suit not in Card.suits:
            raise ValueError(
                f"'{suit}' is not a valid suit. Acceptable values are {', '.join(Card.suits)}")
        if value not in Card.values:
            raise ValueError(
                f"'{value}' is not a valid card value. Acceptable values are {', '.join(Card.values)}")
        self.suit = suit
        self.value = value
