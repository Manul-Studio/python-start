#CW1
import re

hand = open('mbox.txt')
regex = input('Podaj wyrazenie regularne: ')
count = 0
for line in hand:
    line = line.rstrip()
    if re.findall(regex, line):
        count = count+1

print('mbox.txt ma', count, 'linii pasujących do', regex)

#CW2
name = input('Podaj nazwę pliku: ')
hand = open(name)
count = 0
sum = 0
lst = list()
for line in hand:
    line = line.rstrip()
    x = re.findall('^New.*: ([0-9]+)', line)
    for numbers in x:
        numbers = int(numbers)
        sum = sum + numbers
        count = count + 1
print(int(sum/count))
