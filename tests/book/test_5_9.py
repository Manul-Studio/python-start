from unittest import TestCase


class Zadanie_5_9:
    def wprowadz_liczbe(self, liczba):
        return True

    def pokaz_wynik_5_9_1(self):
        return 'do napisania wariant 1'

    def pokaz_wynik_5_9_2(self):
        return 'do napisania wariant 2'

    '''
    Command-line interface
    '''

    def run_cli(self):
        while True:
            n = input('> ')
            if n == 'done':
                break
            try:
                x = float(n)
            except:
                print('tylko liczba')
                continue

            self.wprowadz_liczbe(x)

        print(self.pokaz_wynik_5_9_1())


class Test(TestCase):
    def test_zadanie_5_9_1(self):
        zadanie = Zadanie_5_9()
        zadanie.wprowadz_liczbe(4)
        zadanie.wprowadz_liczbe(5)
        zadanie.wprowadz_liczbe(7)

        self.assertEqual(zadanie.pokaz_wynik_5_9_1(), '16 3 5.333333333333333')

    def test_zadanie_5_9_2(self):
        zadanie = Zadanie_5_9()
        zadanie.wprowadz_liczbe(4)
        zadanie.wprowadz_liczbe(5)
        zadanie.wprowadz_liczbe(7)

        self.assertEqual(zadanie.pokaz_wynik_5_9_2(), '16 3 7 4')

    def test_zadanie_5_9_2_B(self):
        zadanie = Zadanie_5_9()
        zadanie.wprowadz_liczbe(-10)
        zadanie.wprowadz_liczbe(0)
        zadanie.wprowadz_liczbe(0)
        zadanie.wprowadz_liczbe(10)

        self.assertEqual(zadanie.pokaz_wynik_5_9_2(), '0 4 10 -10')

    def test_run_cli(self):
        zadanie = Zadanie_5_9()
        zadanie.run_cli()

