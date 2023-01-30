#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import time
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from game import Game
from player import Player


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.vertical = QtWidgets.QVBoxLayout()
        self.horizontal = QtWidgets.QHBoxLayout()
        self.horizontal.insertLayout(0, self.vertical)

        self.setCentralWidget(QtWidgets.QWidget())
        self.centralWidget().setLayout(self.horizontal)

        self.init_window()

        self.init_buttons()

        self.players = self.get_players()

        self.game = Game(self.scene, self.players, self.rules)

    def init_window(self):
        self.setWindowTitle("Casino")
        self.setGeometry(500, 400, 750, 550)
        self.show()

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 600, 500)

        self.view = QtWidgets.QGraphicsView()
        self.view.setScene(self.scene)
        self.view.show()

        self.horizontal.addWidget(self.view)

    def init_buttons(self):
        self.next_button = QtWidgets.QPushButton("Next turn")
        self.next_button.clicked.connect(lambda: self.next_turn())
        self.vertical.addWidget(self.next_button)

        self.take_button = QtWidgets.QPushButton("Take cards")
        self.take_button.clicked.connect(lambda: self.game.take())
        self.vertical.addWidget(self.take_button)

        self.save_button = QtWidgets.QPushButton("Save game")
        self.save_button.clicked.connect(lambda: self.game.save())
        self.vertical.addWidget(self.save_button)

        self.load_button = QtWidgets.QPushButton("Load game")
        self.load_button.clicked.connect(lambda: self.game.load())
        self.vertical.addWidget(self.load_button)

        self.exit_button = QtWidgets.QPushButton("Exit")
        self.exit_button.clicked.connect(lambda: exit())
        self.vertical.addWidget(self.exit_button)

        self.label = QtWidgets.QLabel("Welcome")
        self.vertical.addWidget(self.label)
        self.label.setAlignment(Qt.AlignHCenter)

    def get_players(self):
        players = []
        correct_input = False
        while not correct_input:
            rules = input("Which ruleset? (1/2)\n")
            if int(rules) == 1:
                self.rules = 1
                correct_input = True
            elif int(rules) == 2:
                self.rules = 2
                correct_input = True
        correct_input = False
        while not correct_input:
            player_count = input("How many players?\n")
            if player_count.isdigit():
                correct_input = True
        for i in range(int(player_count)):
            name = input("Give name for player {} \n".format(i + 1))
            players.append(Player(name))
            print("Welcome to the table {}\n".format(name))
        print("Game starting")
        return players

    def next_turn(self):
        if self.game.turns_left == 0:
            for card in self.game.cards:
                if card is not None:
                    self.game.players[self.game.last_take].cards.append(card)
            self.game.points()
            points = []
            for player in self.game.players:
                points.append(player.points)
            if self.rules == 1:
                winner = points.index(max(points))
            else:
                winner = points.index(min(points))
            self.win(winner)
        elif self.game.next_turn():
            winner = self.game.points()
            if winner != -1:
                for card in self.game.cards:
                    if card is not None:
                        self.game.players[self.game.last_take].cards.append(card)
                self.win(winner)
            self.game.turn += 1
            self.game.next += 1
            if self.game.turn == len(self.game.players):
                self.game.turn = 0
            if self.game.next == len(self.game.players):
                self.game.next = 0
            self.label.setText("Player {} turn".format(self.game.players[self.game.turn].name))
            self.game.turns_left -= 1

    def win(self, winner):
        self.scene.clear()
        win = QtWidgets.QLabel("{} Won the game!".format(self.game.players[winner].name))
        self.scene.addWidget(win)
        i = 0
        for player in self.game.players:
            point = QtWidgets.QLabel("{}: {} points".format(player.name, player.points))
            self.scene.addWidget(point)
            point.move(20 + 100 * i, 200)
            i += 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
