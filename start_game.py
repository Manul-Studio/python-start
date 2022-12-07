# starting the game
from TicTacToe.TicTacToe import TicTacToe, boardField

tic_tac_toe = TicTacToe()
tic_tac_toe.start()

tic_tac_toe.set_spot(1, 1, boardField["player1"])
tic_tac_toe.set_spot(1, 2, boardField["player2"])
tic_tac_toe.set_spot(2, 2, boardField["player1"])

tic_tac_toe.draw_board()
