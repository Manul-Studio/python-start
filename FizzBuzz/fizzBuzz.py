'''
Funkcja przyjmuje liczbe naturalna większą bądz równą 1

dla zadanej liczby sprawdza wszystkie warunki
- jezeli jest podzielna przez 3 to komunikuje to dodajac Fizz w odpowiedzi
- jezeli jest podzielna przez 5 to komunikuje to dodajac Bazz w odpowiedzi
- jeżeli wczesniejszy warunek nie zostal spelniony, zwracana jest w odpowiedzi zadana liczba
'''

def fizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return str(num)
