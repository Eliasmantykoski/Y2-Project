from deck import Deck


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.cards = []
        self.hand = [None]*4
        self.mokki = 0

    def take_cards(self):
        while len(self.hand) < 4:
            self.hand.append(Deck.get_card())

    def count_points(self):
        self.points = self.mokki
        for card in self.cards:
            if card.value == 1:
                self.points += 1
            elif card.value == 10 and card.suit == "d":
                self.points += 2
            elif card.value == 2 and card.suit == "s":
                self.points += 1

    def count_club(self):
        club = 0
        for card in self.cards:
            if card.suit == "c":
                club += 1
        return club


