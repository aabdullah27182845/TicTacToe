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


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.availableMoves()) == 9:
            square = random.choice(game.availableMoves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = '0' if player == 'X' else 'X'

        if state.currentWinner == other_player:
            return {'position': None,
                    'score': ((state.num_empty_squares() + 1) if other_player == max_player else  \
                    -1 * (state.num_empty_squares() + 1))}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}


        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.availableMoves():

            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.currentWinner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best 
        




