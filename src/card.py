

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        self.graphic = None
        self.handval = val
        if val == 1:
            self.handval = 14
        if suit == "d" and val == 10:
            self.handval = 16
        if suit == "s" and val == 2:
            self.handval = 15

    def get_suit(self):
        return self.suit

    def get_val(self):
        return self.value
