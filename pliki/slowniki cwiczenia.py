#CW2
fname = input("Podaj nazwę: ")
fhand = open(fname)
d = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 and len(words) < 3:
        continue
    if words[0]!= 'From':
        continue
    d[words[2]] = d.get(words[2], 0) +1
print(d)

#CW3 
fname = input("Podaj nazwę: ")
fhand = open(fname)
d = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 and len(words) < 3:
        continue
    if words[0]!= 'From':
        continue
    d[words[1]] = d.get(words[1], 0) +1
print(d)

#CW 4
fname = input("Podaj nazwę: ")
fhand = open(fname)
d = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 and len(words) < 3:
        continue
    if words[0]!= 'From':
        continue
    d[words[1]] = d.get(words[1], 0) +1

biggest = None
count = None
for k,v in d.items():
    if biggest is None or k > biggest:
        biggest = k
        count = v
print(biggest, count)

#CW5
fname = input("Podaj nazwę: ")
fhand = open(fname)
d = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 and len(words) < 3:
        continue
    if words[0] != 'From':
        continue

    mail = words[1].split('@')
    d[mail[1]] = d.get(mail[1], 0) + 1
print(d)



