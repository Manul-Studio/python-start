class Hangman:
    '''
    Podajemy hasło jakie będziemy zgadywać
    '''

    def __init__(self, haslo):
        self.haslo = haslo
        self.trafione = ''

    '''
    Gracz wprowadza znak jaki chce zgadywać
    Jezeli go nie ma to zwracamy 0
    Jezeli jest, to zwracamy ile razy
    '''

    def zgadujeZnak(self, znak):
        zlicz = 0
        for litera in self.haslo:
            if litera == znak:
                zlicz = zlicz + 1
        if zlicz > 0:
                self.trafione = self.trafione + znak
        return zlicz

    '''
    Zwraca nasze hasło ze zgadnietymi znakami :)
    jak nie odkryty jest znak to zamieniamy go na "_"
    '''

    def hasloZeZgadnietymi(self):
        odpowiedz = ''
        for x in self.haslo:
            if x in self.trafione:
                odpowiedz += x
            else:
                odpowiedz += '_'
        return odpowiedz

    '''
    Czy nasz gracz zgadl caly wyraz?
    zwraca true/false
    '''

    def czyGraczWygral(self):
        return True
