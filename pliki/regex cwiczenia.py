#CW1
import re

hand = open('mbox.txt')
regex = input('Podaj wyrazenie regularne: ')
count = 0
for line in hand:
    if re.search(regex, line):
        count = count+1

print('mbox.txt ma', count, 'linii pasujących do', regex)

#CW2
name = input('Podaj nazwę pliku: ')
hand = open(name)
inp = hand.read()
x = re.findall('New Revision: ([0-9]+)', inp)
lst = list(map(int, x))
print(int(sum(lst)/len(lst)))
