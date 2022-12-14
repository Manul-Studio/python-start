from unittest import TestCase

from Hangman.Hangman import Hangman


class Test(TestCase):
    def test_hangman_banana_1(self):
        hangman = Hangman('banana')
        self.assertEqual(hangman.trafione, '')

        self.assertEqual(hangman.zgadujeZnak('a'), 3)
        self.assertEqual(hangman.trafione, 'a')

        self.assertEqual(hangman.zgadujeZnak('z'), 0)
        self.assertEqual(hangman.trafione, 'a')

        self.assertEqual(hangman.zgadujeZnak('b'), 1)
        self.assertEqual(hangman.trafione, 'ab')

        self.assertEqual(hangman.hasloZeZgadnietymi(), 'ba_a_a')
        return 1
        self.assertEqual(hangman.czyGraczWygral(), False)
