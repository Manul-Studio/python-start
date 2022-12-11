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

    def __is_all_fields_same(self, a, b, c, player):
        if a == b and b == c and c == player:
            return True
        return False


    def is_player_win(self, player):

        for x in range(3):
            ''' Poziome linie '''
            if self.__is_all_fields_same(self.board[0][x], self.board[1][x], self.board[2][x], player):
                return True

            ''' Pionowe linie '''
            if self.__is_all_fields_same(self.board[x][0], self.board[x][1], self.board[x][2], player):
                return True

        ''' Przekatne '''
        if self.__is_all_fields_same(self.board[0][0], self.board[1][1], self.board[2][2], player):
            return True

        if self.__is_all_fields_same(self.board[2][0], self.board[1][1], self.board[0][2], player):
            return True

        '''Nie udalo sie wykryc zwycięstwa gracza '''
        return False

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                self.printXO(self.board[i][j])
                '''
                print(self.board[i][j], end=" ")
                print("i = %s  j = %s" % (i, j))
                '''
            print("")
            print("-----")

    def printXO(self, pole):

        if pole == 1:
            print("X", end=" ")
            return True

        if pole == 2:
            print("O", end=" ")
            return True

        print("-", end=" ")




        # todo Narysowac prawdziwa plansze :D
        # player1 = "X"
        # player2 = "O"
        # puste pole "-"
'''
        print() #enter
        print('O|-|O')
        print('-|X|-')
        print('-|-|O')
        print() #enter
'''