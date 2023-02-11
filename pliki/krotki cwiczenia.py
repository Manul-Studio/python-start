# CW1
fname = input("Podaj nazwe: ")
fhand = open(fname)
d = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 and len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    d[words[1]] = d.get(words[1], 0) + 1

lst = [(v, k) for k, v in d.items()]

lst.sort(reverse=True)
k1, v1 = lst[0]
print(k1, v1)

# CW2
fname = input("Podaj nazwe: ")
fhand = open(fname)
d = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 and len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    hour = words[5].split(':')
    d[hour[0]] = d.get(hour[0], 0) + 1

lst = [(k,v) for k,v in d.items()]
lst.sort()
for key, val in lst:
    print(key, val)

#CW3
fname = input("Podaj nazwe: ")
fhand = open(fname)

d = dict()
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if letter.isalpha():
                d[letter] = d.get(letter, 0) + 1

lst = list()
lst = [(k,v) for v,k in d.items()]
lst.sort(reverse=True)
sum =0
for v, k in lst:
    sum = sum+v
    print(k, v)
print(sum)
for v, k in lst:
    czestosc = round((v/sum)*100,2)
    print(k, czestosc, '%')


