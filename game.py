from player import *
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.currentWinner = None

    def printBoard(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod
    def printBoardNums():
        numberBoard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberBoard:
            print('| ' + ' | '.join(row) + ' |')

    def availableMoves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)

        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinnder = letter
            return True
        else:
            return False

    def winner(self, square, letter):

        rowIndex = square // 3
        row = self.board[rowIndex*3 : (rowIndex + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        colIndex = square % 3
        column = [self.board[colIndex + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False
            

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.printBoardNums()

    letter = 'X'

    while game.empty_squares():
        if letter == '0':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.printBoard()
                print('')

            if game.winner(square, letter):
                if print_game:
                    print(letter + " wins")
                return letter

            letter = '0' if letter == 'X' else 'X'


        time.sleep(0.8)
            

def main():
    pass

if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('0')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
