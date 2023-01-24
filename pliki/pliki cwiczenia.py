#ćwiczenie 1 7.12
fhand = open(input('Podaj nazwę: '))
x = fhand.read()
print(x.upper())



#ćwiczenie 2 7.12 + ćwiczenie 3
fname = input('Podaj nazwę: ')
if fname == 'trele morele':
    print('co za bzdury')
    exit()
try:
    fhand = open(fname)
except:
    print('nie można otworzyc pliku')
    exit()
zlicz = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    start = line.find(': ')
    liczba = float(line[start+1:])
    zlicz = zlicz + 1
    total = total + liczba

srednia = total / zlicz
print('średni poziom pewności spamu: ', srednia)
