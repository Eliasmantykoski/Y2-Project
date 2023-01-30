from deck import Deck
from player import Player
from card import Card
import itertools

from card_graphics import CardGraphic


class Game:
    def __init__(self, scene, players, rules):
        self.scene = scene
        self.rules = rules
        self.cards = [None]*48
        self.player_cards = [None]*4
        self.deck = Deck()
        self.players = players
        self.init_cards()
        self.deal_cards()
        self.turn = len(players)-1
        self.next = 0
        self.played = True
        self.last_take = 0
        self.turns_left = 48

    def init_cards(self):
        for x in range(4):
            card = self.deck.get_card()
            card.graphic = CardGraphic(card, self.scene)
            self.scene.addItem(card.graphic)
            card.graphic.setPos(15 + x*150, 30)
            self.cards[x] = card
            card.graphic.setOpacity(0.6)

    def next_turn(self):
        if self.played:
            self.played = False
            for card in self.player_cards:
                if card is not None:
                    if card.graphic.selected:
                        self.players[self.turn].cards.append(card)
                        self.players[self.turn].hand[self.players[self.turn].hand.index(card)] = None
                        card.graphic.selected = False
                    self.scene.removeItem(card.graphic)
            self.fill_hand()
            self.draw_player_cards(self.next)
            return True
        elif self.add():
            self.played = False
            self.add_to_table()
            for card in self.player_cards:
                if card is not None:
                    card.graphic.selected = False
                    self.scene.removeItem(card.graphic)
            self.fill_hand()
            self.draw_player_cards(self.next)
            self.update_table()
            return True

        else:
            print("Make a move")
            return False

    def deal_cards(self):
        for player in self.players:
            for i in range(4):
                player.hand[i] = self.deck.get_card()

    def draw_player_cards(self, index):
        self.player_cards = [None]*4
        for x in range(4):
            if self.players[index].hand[x] is not None:
                if self.players[index].hand[x].graphic is None:
                    self.players[index].hand[x].graphic = CardGraphic(self.players[index].hand[x], self.scene)
                self.scene.addItem(self.players[index].hand[x].graphic)
                self.players[index].hand[x].graphic.setOpacity(0.6)
                self.players[index].hand[x].graphic.setPos(15 + x * 150, 320)
                self.player_cards[x] = self.players[index].hand[x]

    def take(self):
        if self.valid_move():
            cards = 0
            selected = 0
            for card in self.cards:
                self.last_take = self.turn
                if card is not None:
                    cards += 1
                    if card.graphic.selected:
                        selected += 1
                        self.players[self.turn].cards.append(card)
                        self.scene.removeItem(card.graphic)
                        self.cards[self.cards.index(card)] = None
            if cards == selected:
                self.players[self.turn].mokki += 1
                print("mökki!")
        else:
            print("invalid move")

    def valid_move(self):
        player_selected = []
        for card in self.players[self.turn].hand:
            if card is not None:
                if card.graphic.selected:
                    player_selected.append(card)
        if len(player_selected) == 1:
            player_val = player_selected[0].handval
            table_vals = []
            for card in self.cards:
                if card is not None:
                    if card.graphic.selected:
                        table_vals.append(card.get_val())
            if player_val == sum(table_vals):
                self.played = True
                return True
        else:
            return False

    def move_available(self):
        table = []
        for card in self.cards:
            if card is not None:
                table.append(card.value)
        hand = []
        for card in self.players[self.turn].hand:
            if card is not None:
                hand.append(card.value)
        sums = []
        for n in range(1, 7):
            combos = list(itertools.combinations(table, n))
            for combo in combos:
                sums.append(sum(combo))
        for num in hand:
            if num in sums:
                return True
        return False

    def fill_hand(self):
        for i in range(4):
            if self.players[self.turn].hand[i] is None:
                self.players[self.turn].hand[i] = self.deck.get_card()

    def add_to_table(self):
        i = 0
        while self.cards[i] is not None:
            i += 1
        index = 0

        """while not self.players[self.turn].hand[index].graphic.selected:
            index += 1"""

        for card in self.players[self.turn].hand:
            if card is not None:
                if card.graphic.selected:
                    break
            index += 1
        self.cards[i] = self.players[self.turn].hand[index]
        self.scene.removeItem(self.players[self.turn].hand[index].graphic)
        self.players[self.turn].hand[index] = None

    def add(self):
        if self.rules == 2 and self.move_available():
            return False
        for card in self.cards:
            if card is not None:
                if card.graphic.selected:
                    return False
        selected = 0
        for card in self.players[self.turn].hand:
            if card is not None:
                if card.graphic.selected:
                    selected += 1
        if selected == 1:
            return True
        else:
            return False

    def update_table(self):
        for card in self.cards:
            if card is not None:
                self.scene.removeItem(card.graphic)
        x = 0
        for card in self.cards:
            if card is not None:
                card.graphic = CardGraphic(card, self.scene)
                self.scene.addItem(card.graphic)
                card.graphic.setPos(15 + x * 150, 30)
                card.graphic.setOpacity(0.6)
                self.cards[x] = card
                if x < 4:
                    self.scene.setSceneRect(0, 0, 600, 500)
                else:
                    self.scene.setSceneRect(0, 0, 200*x, 500)
            x += 1

    def points(self):
        clubs = []
        cards = []
        for player in self.players:
            player.count_points()
            clubs.append(player.count_club())
            cards.append(len(player.cards))
        if max(clubs) > 0:
            self.players[clubs.index(max(clubs))].points += 2
        if max(cards) > 0:
            self.players[cards.index(max(cards))].points += 1
        index = 0
        if self.rules == 1:
            for player in self.players:
                if player.points > 15:
                    print("{} is the winner".format(player.name))
                    return index
                index += 1
        return -1

    def save(self):
        f = open("save.txt", "w+")
        f.write(str(len(self.players)) + "\n")
        f.write(str(self.turn) + "\n")
        for player in self.players:
            f.write(player.name + "\n")
            f.write(str(player.mokki) + "\n")
            for card in player.hand:
                if card is not None:
                    f.write(card.suit + str(card.value) + " ")
            f.write("\n")
            if len(player.cards) == 0:
                f.write("0\n")
            else:
                for card in player.cards:
                    f.write(card.suit + str(card.value) + " ")
                f.write("\n")
        for card in self.cards:
            if card is not None:
                f.write(card.suit + str(card.value) + " ")
        f.write("\n")
        f.close()
        print("Game saved to 'save.txt'\nExiting program")
        exit()

    def load(self):
        for card in self.cards:
            if card is not None:
                self.scene.removeItem(card.graphic)
        self.deck = Deck()
        try:
            f = open("save.txt", "r")
            playercount = int(f.readline())
            players = []
            turn = int(f.readline())
            if turn == 0:
                self.turn = playercount - 1
            else:
                self.turn = turn - 1
            self.next = turn
            for i in range(playercount):
                name = f.readline()
                player = Player(name)
                player.mokki = int(f.readline())
                players.append(player)
                hand = f.readline().strip()
                cards_str = hand.split(" ")
                for j in range(4):
                    suit = cards_str[j][0]
                    val = int(cards_str[j][1:])
                    card = Card(suit, val)
                    self.deck.remove(suit, val)
                    card.graphic = CardGraphic(card, self.scene)
                    players[i].hand[j] = card
                cards = f.readline().strip()
                if cards.startswith("0"):
                    pass
                else:
                    cards_str = cards.split(" ")
                    for card_str in cards_str:
                        suit = card_str[0]
                        val = int(card_str[1:])
                        card = Card(suit, val)
                        self.deck.remove(suit, val)
                        players[i].cards.append(card)
            self.players = players
            table = f.readline().strip()
            if table is not None:
                table_list = table.split(" ")
                self.cards = [None]*48
                x = 0
                for card_str in table_list:
                    suit = card_str[0]
                    val = int(card_str[1:])
                    card = Card(suit, val)
                    self.deck.remove(suit, val)
                    self.cards[x] = card
                    x += 1
        except:
            print("error loading from file")
        self.player_cards = self.players[0].hand
        self.update_table()
        self.turns_left = len(self.deck.cards)
