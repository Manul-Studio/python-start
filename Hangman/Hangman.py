class Hangman:
    '''
    Podajemy hasło jakie będziemy zgadywać
    '''

    def __init__(self, haslo):
        self.haslo = haslo

    '''
    Gracz wprowadza znak jaki chce zgadywać
    Jezeli go nie ma to zwracamy 0
    Jezeli jest, to zwracamy ile razy
    '''

    def zgadujeZnak(self, znak):
        return 0

    '''
    Zwraca nasze hasło ze zgadnietymi znakami :)
    jak nie odkryty jest znak to zamieniamy go na "_"
    '''

    def hasloZeZgadnietymi(self):
        return self.haslo

    '''
    Czy nasz gracz zgadl caly wyraz?
    zwraca true/false
    '''

    def czyGraczWygral(self):
        return True