#Cw4
fname = input("Podaj nazwę: ")
fhand = open(fname)
lst = list()
for line in fhand:
    words = line.rstrip()
    words = line.split()
    for words1 in words:
        if words1 not in lst:
            lst.append(words1)
lst.sort()
print(lst)

#Cw5
fname = input("Podaj nazwę: ")
fhand = open(fname)
count = 0
for line in fhand:
    line = line.rstrip()
    if len(line) == 0 and len(line) < 3:
        continue
    if not line.startswith('From'):
        continue
    count = count + 1
    words = line.split()
    print(words[1])
print('Mamy ', count, 'linii, w których From jest pierwszym wyrazem')

#Cw6
lst = list()
while True:
    liczba = input('Wprowadź liczbę: ')
    if liczba == 'done':
        break
    lst.append(liczba)
print('Największa:', max(lst))
print('Najmniejsza:', min(lst))