'''
imie nazwisko: jakub łysiak
ID: 05
temat zadania - Sprawdzian rekurencja i iteracja
'''

tbl = [7, 2, 9, 3, 1, 2, 0, 5]


def rekurencja(lista, i):
    if i == -1:
        return
    print(lista[i], end=' ')
    rekurencja(lista, i - 1)


def iteracja(lista):
    i = len(lista) - 1
    while i >= 0:
        print(lista[i], end=' ')
        i = i - 1


print("lista przed", tbl)
print("lista po rekurencji: ", end='')
rekurencja(tbl, len(tbl) - 1)
print("\nlista po iteracji: ", end='')
iteracja(tbl)
