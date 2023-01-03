from unittest import TestCase


class Zadanie_5_9:
    def __init__(self):
        self.liczby = []

    def wprowadz_liczbe(self, liczba):
        self.liczby.append(liczba)
        return True

    def pokaz_wynik_5_9_1(self):
        suma = 0
        ile = 0
        srednia = 0
        for x in self.liczby:
            suma += x
            ile += 1

        srednia = suma/ile

        return str(suma) + " " + str(ile) + " " + str(srednia)

    def pokaz_wynik_5_9_2(self):
        suma = 0
        ile = 0
        for x in self.liczby:
            suma += x
            ile += 1

        maxi = max(self.liczby)
        mini = min(self.liczby)

        return str(suma) + " " + str(ile) + " " + str(maxi) + " " + str(mini)


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

