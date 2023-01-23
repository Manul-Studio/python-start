#Cwiczenie 1  8.13

def chop(list):
    del list[0]
    del list[-1]


def middle(list):
    nowa = list[1:]
    del nowa[-1]
    return nowa


lista = [1, 4, 6, 2]

x = chop(lista)
print(x)

print(lista)

lista2 = [2, 5, 7, 8]

y = middle(lista2)
print(y)