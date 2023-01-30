from card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.fill()

    def get_card(self):
        if len(self.cards) == 0:
            return None
        index = random.randint(0, len(self.cards)-1)
        return self.cards.pop(index)

    def fill(self):
        for suit in ["s", "c", "h", "d"]:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    def remove(self, suit, val):
        for card in self.cards:
            if card.suit == suit and card.value == val:
                self.cards.remove(card)