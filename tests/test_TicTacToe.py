from unittest import TestCase

from TicTacToe.TicTacToe import TicTacToe, boardField


class TestTicTacToe(TestCase):
    def setUp(self):
        self.tic_tac_toe = TicTacToe()
        self.tic_tac_toe.start()


class TestTicTacToeWin(TestTicTacToe):
    def test_player1_no_winner(self):
        self.tic_tac_toe.set_spot(0, 0, boardField["player1"])
        self.tic_tac_toe.set_spot(0, 1, boardField["player1"])
        self.tic_tac_toe.set_spot(1, 2, boardField["player1"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player1"]), False)


    def test_player1_win_scenariusz_poziom_0(self):
        self.tic_tac_toe.set_spot(0, 0, boardField["player1"])
        self.tic_tac_toe.set_spot(0, 1, boardField["player1"])
        self.tic_tac_toe.set_spot(0, 2, boardField["player1"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player1"]), True)

    def test_player1_win_scenariusz_poziom_1(self):
        self.tic_tac_toe.set_spot(1, 0, boardField["player1"])
        self.tic_tac_toe.set_spot(1, 1, boardField["player1"])
        self.tic_tac_toe.set_spot(1, 2, boardField["player1"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player1"]), True)

    def test_player1_win_scenariusz_poziom_2(self):
        self.tic_tac_toe.set_spot(2, 0, boardField["player1"])
        self.tic_tac_toe.set_spot(2, 1, boardField["player1"])
        self.tic_tac_toe.set_spot(2, 2, boardField["player1"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player1"]), True)

    def test_player1_win_scenariusz_pionowo_0(self):
        self.tic_tac_toe.set_spot(0, 0, boardField["player1"])
        self.tic_tac_toe.set_spot(1, 0, boardField["player1"])
        self.tic_tac_toe.set_spot(2, 0, boardField["player1"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player1"]), True)

    def test_player1_win_scenariusz_pionowo_1(self):
        self.tic_tac_toe.set_spot(0, 1, boardField["player1"])
        self.tic_tac_toe.set_spot(1, 1, boardField["player1"])
        self.tic_tac_toe.set_spot(2, 1, boardField["player1"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player1"]), True)

    def test_player1_win_scenariusz_pionowo_2(self):
        self.tic_tac_toe.set_spot(0, 2, boardField["player1"])
        self.tic_tac_toe.set_spot(1, 2, boardField["player1"])
        self.tic_tac_toe.set_spot(2, 2, boardField["player1"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player1"]), True)

    def test_player1_win_scenariusz_skos_1(self):
        self.tic_tac_toe.set_spot(0, 0, boardField["player1"])
        self.tic_tac_toe.set_spot(1, 1, boardField["player1"])
        self.tic_tac_toe.set_spot(2, 2, boardField["player1"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player1"]), True)

    def test_player1_win_scenariusz_skos_2(self):
        self.tic_tac_toe.set_spot(2, 0, boardField["player1"])
        self.tic_tac_toe.set_spot(1, 1, boardField["player1"])
        self.tic_tac_toe.set_spot(0, 2, boardField["player1"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player1"]), True)

    def test_player1_no_winner(self):
        self.tic_tac_toe.set_spot(0, 0, boardField["player1"])
        self.tic_tac_toe.set_spot(0, 1, boardField["player1"])
        self.tic_tac_toe.set_spot(1, 2, boardField["player1"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player1"]), False)


    def test_player2_win_scenariusz_poziom_0(self):
        self.tic_tac_toe.set_spot(0, 0, boardField["player2"])
        self.tic_tac_toe.set_spot(0, 1, boardField["player2"])
        self.tic_tac_toe.set_spot(0, 2, boardField["player2"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player2"]), True)

    def test_player2_win_scenariusz_poziom_1(self):
        self.tic_tac_toe.set_spot(1, 0, boardField["player2"])
        self.tic_tac_toe.set_spot(1, 1, boardField["player2"])
        self.tic_tac_toe.set_spot(1, 2, boardField["player2"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player2"]), True)

    def test_player2_win_scenariusz_poziom_2(self):
        self.tic_tac_toe.set_spot(2, 0, boardField["player2"])
        self.tic_tac_toe.set_spot(2, 1, boardField["player2"])
        self.tic_tac_toe.set_spot(2, 2, boardField["player2"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player2"]), True)

    def test_player2_win_scenariusz_pionowo_0(self):
        self.tic_tac_toe.set_spot(0, 0, boardField["player2"])
        self.tic_tac_toe.set_spot(1, 0, boardField["player2"])
        self.tic_tac_toe.set_spot(2, 0, boardField["player2"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player2"]), True)

    def test_player2_win_scenariusz_pionowo_1(self):
        self.tic_tac_toe.set_spot(0, 1, boardField["player2"])
        self.tic_tac_toe.set_spot(1, 1, boardField["player2"])
        self.tic_tac_toe.set_spot(2, 1, boardField["player2"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player2"]), True)

    def test_player2_win_scenariusz_pionowo_2(self):
        self.tic_tac_toe.set_spot(0, 2, boardField["player2"])
        self.tic_tac_toe.set_spot(1, 2, boardField["player2"])
        self.tic_tac_toe.set_spot(2, 2, boardField["player2"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player2"]), True)

    def test_player2_win_scenariusz_skos_1(self):
        self.tic_tac_toe.set_spot(0, 0, boardField["player2"])
        self.tic_tac_toe.set_spot(1, 1, boardField["player2"])
        self.tic_tac_toe.set_spot(2, 2, boardField["player2"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player2"]), True)

    def test_player2_win_scenariusz_skos_2(self):
        self.tic_tac_toe.set_spot(2, 0, boardField["player2"])
        self.tic_tac_toe.set_spot(1, 1, boardField["player2"])
        self.tic_tac_toe.set_spot(0, 2, boardField["player2"])

        self.assertEqual(self.tic_tac_toe.is_player_win(boardField["player2"]), True)