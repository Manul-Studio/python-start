'''
Funkcja przyjmuje liczbe naturalna większą bądz równą 1

dla zadanej liczby sprawdza wszystkie warunki
- jezeli jest podzielna przez 3 to komunikuje to dodajac Fizz w odpowiedzi
- jezeli jest podzielna przez 5 to komunikuje to dodajac Bazz w odpowiedzi
- jeżeli wczesniejszy warunek nie zostal spelniony, zwracana jest w odpowiedzi zadana liczba
'''

def fizzBuzz(num):
    fizz = num % 3 == 0
    buzz = num % 5 == 0

    if fizz and buzz:
        return "FizzBuzz"
    elif buzz:
        return "Buzz"
    elif fizz:
        return "Fizz"
    # else: <- nie jest to blad, natomiast lepiej jest po prostu nie pisac jezeli nie jest faktycznie ważne - po prostu kod jest "prostszy i krótszy"
    return str(num)
'''
kill me
'''