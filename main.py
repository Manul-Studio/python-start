
#5.9 ćwiczenie
while True:
        n = input('> ')
        if n == 'done':
            break
        try:
            x = float(n)
        except:
            print('tylko liczba')
            continue

print('all done')


# długosć napisu
fruit = "banana"
x = len(fruit)
print(x)
length = len(fruit)
last = fruit[length - 1]
print(last)

fruit = 'banana'

index = 5
while index >= 0:  # jak idzie od początku to index < len(fruit)/ index< 6(tyle ma banana)
    letter = fruit[index]
    print(letter)
    index = index - 1
    # wyświetlanie 'banan' od końca    index +1 od początku

for x in fruit:
    print(x)

# wycinki

s = 'Monty Python'
print(s[0:5])  # wyswietlanie od znaku 0 do 5

fruit = 'apple'
print(fruit[:3])  # printuje pierwsze 3 od poczatku(pominięcie 1 indexu)
print(fruit[3:])  # od 3 znaku do końca
print(fruit[3:3])  # pusty napis
print(fruit[:])  # cały napis

greeting = 'Hello World'
new_greeting = 'h' + greeting[1:]
print(new_greeting)

# przechodzenie w pętli i zliczanie
word = 'banan'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.
def count(w, l):
    counter = 0
    for char in w:
        if char == l:
            counter = counter + 1
    print(counter)


count('banana', 'a')
count('dupa', 'd')

if word == 'banan':
    print('Wszystko ok, to banany')

duzy = 'banan'
new_duzy = duzy.upper()
print(new_duzy)  # wywoływanie metody-> zamiast składni funkcji upper(duzy) używa składni metody duzy.upper()

owoc = 'banan'
znajdz = owoc.find('a')  # szuka pozycji jednego napisu w drugim
print(znajdz)

line = '   proszę '
print(line.strip())  # usuwanie białych znakow

line2 = 'Miłego'
line2.startswith('i')

owo = 'banan'
print(owo.count('a', 0, len(owo)))

data = 'cośtam@costam.popop 4352 423'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos + 1:sppos]
print(host)

print('Przez %d lata widziałem  %g %s.' % (3, 0.1, 'wielbłąda')) # %d liczba całkowita, %g przecinkowa, %s string
