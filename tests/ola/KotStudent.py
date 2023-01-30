import math
from unittest import TestCase
import math


class KotStudent:

    def poleKola(self, promien):
        pole = math.pi * pow(promien, 2)
        return round(pole, 2)

    def objetoscWalca(self, promien, wysokosc):
        objetoscw = self.poleKola(promien) * wysokosc
        return round(objetoscw, 2)

    def objetoscStozka(self, promien, wysokosc):
        objetoscs = 1 / 3 * self.objetoscWalca(promien, wysokosc)
        return round(objetoscs, 2)


class Test(TestCase):
    def test_kotstudent1(self):
        kot = KotStudent()

        self.assertEqual(kot.poleKola(1), 3.14)

    def test_kotstudent2(self):
        kot = KotStudent()

        self.assertEqual(kot.poleKola(3), 28.27)

    def test_kotstudent3(self):
        kot = KotStudent()

        self.assertEqual(kot.poleKola(5), 78.54)

    def test_kotstudent4(self):
        kot = KotStudent()

        self.assertEqual(kot.poleKola(11), 380.13)

    def test_kotstudent5(self):
        kot = KotStudent()

        self.assertEqual(kot.poleKola(42), 5541.77)

    def test_kotstudent6(self):
        kot = KotStudent()

        self.assertEqual(kot.poleKola(101), 32047.39)

    def test_kotstudentwalec1(self):
        kot = KotStudent()

        self.assertEqual(kot.objetoscWalca(3, 3), 84.81)

    def test_kotstudentwalec2(self):
        kot = KotStudent()

        self.assertEqual(kot.objetoscWalca(5, 5), 392.7)

    def test_kotstudentwalec3(self):
        kot = KotStudent()

        self.assertEqual(kot.objetoscWalca(11, 11), 4181.43)

    def test_kotstudentstozek1(self):
        kot = KotStudent()

        self.assertEqual(kot.objetoscStozka(3, 3), 28.27)

    def test_kotstudentstozek2(self):
        kot = KotStudent()

        self.assertEqual(kot.objetoscStozka(5, 5), 130.9)

    def test_kotstudentstozek3(self):
        kot = KotStudent()

        self.assertEqual(kot.objetoscStozka(11, 11), 1393.81)
