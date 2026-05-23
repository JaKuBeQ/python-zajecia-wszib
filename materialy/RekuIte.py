'''
imie nazwisko: jakub łysiak
ID: 05
temat zadania - Sprawdzian rekurencja i iteracja
'''

tbl = [7, 2, 9, 3, 1, 2, 0, 5]


def rekurencja_reverse(lista, i):
    if i == len(lista):
        return
    print(lista[i], end=' ')
    rekurencja_reverse(lista, i + 1)


def iteracja_reverse(lista):
    reversed_list = reversed(lista)
    for item in reversed_list:
        print(item, end=' ')


print("lista przed:", tbl)
print("lista po rekurencji (reverse): ", end='')
rekurencja_reverse(list(reversed(tbl)), 0)
print("\nlista po iteracji (reverse): ", end='')
iteracja_reverse(tbl)