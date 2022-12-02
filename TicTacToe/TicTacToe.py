import random

boardField = {
    "player1": 1,
    "player2": 2,
    "empty": 0
}

"""
Plansza to dwuwymiarowa tablica wygladajaca tak:

0,0 | 0,1 | 0,2
1,0 | 1,1 | 1,2
2,0 | 2,1 | 2,2


Moze miec wartosci:
0 - puste pole
1 - pole gracza 1 (X)
2 - pole gracza 2 (O)


"""
class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(boardField["empty"])
            self.board.append(row)

    def start(self):
        self.create_board()

    def set_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        if self.board[0][0] == player and self.board[0][1] == player and self.board[0][2] == player:
            return True
        if self.board[1][0] == player and self.board[1][1] == player and self.board[1][2] == player:
            return True
        if self.board[2][0] == player and self.board[2][1] == player and self.board[2][2] == player:
            return True
        if self.board[0][0] == player and self.board[1][0] == player and self.board[2][0] == player:
            return True
        if self.board[0][1] == player and self.board[1][1] == player and self.board[2][1] == player:
            return True
        if self.board[0][2] == player and self.board[1][2] == player and self.board[2][2] == player:
            return True
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            return True

        return False

