import math
import random
from game import *


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.availableMoves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')

            try:
                val = int(square)
                if val not in game.availableMoves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square")

        return val
