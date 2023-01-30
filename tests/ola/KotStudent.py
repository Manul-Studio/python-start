import math
from unittest import TestCase
import math

class KotStudent:
    def __init__(self, r, h):
        self.promien = r
        self.wysokosc = h


    def poleKola(self):
        '''pole = math.pi * (self.promien * self.promien)'''
        pole = math.pi * pow(self.promien, 2)
        return round(pole, 2)

    def objetoscWalca(self):
        objetoscw = self.poleKola() * self.wysokosc
        return round(objetoscw, 2)

    def objetoscStozka(self):
        objetoscs = 1/3 * self.objetoscWalca()
        return round(objetoscs, 2)




class Test(TestCase):
    def test_kotstudent1(self):
        kot = KotStudent(1)

        self.assertEqual(kot.poleKola(), 3.14)

    def test_kotstudent2(self):
        kot = KotStudent(3)

        self.assertEqual(kot.poleKola(), 28.27)

    def test_kotstudent3(self):
        kot = KotStudent(5)

        self.assertEqual(kot.poleKola(), 78.54)

    def test_kotstudent4(self):
        kot = KotStudent(11)

        self.assertEqual(kot.poleKola(), 380.13)

    def test_kotstudent5(self):
        kot = KotStudent(42)

        self.assertEqual(kot.poleKola(), 5541.77)

    def test_kotstudent6(self):
        kot = KotStudent(101)

        self.assertEqual(kot.poleKola(), 32047.39)

    def test_kotstudent7walec(self):
        kot = KotStudent(3, 3)

        self.assertEqual(kot.objetoscWalca(), 84.81)

    def test_kotstudent8stozek(self):
        kot = KotStudent(5, 5)

        self.assertEqual(kot.objetoscStozka(), 130.9)



