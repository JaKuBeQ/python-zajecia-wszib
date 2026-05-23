'''
imie nazwisko: jakub łysiak
ID: 05
temat zadania - stragan
'''

stragan = {'Nazwa':['j.m', 'cena', 'ilość'],
           'Gruszki':['kg', '8.50', '3.50'],
           }

tbl = [7, 2, 9, 3, 1, 2, 0, 5]

def rekurencja(lista, i):
    if i == -1:
        return
    print(lista[i])
    rekurencja(lista, i - 1)

def iteracja(lista):
    i = len(lista) - 1
    while i >= 0:
        print(lista[i])
        i = i - 1

print("Wypisanie rekurencyjne:")
rekurencja(tbl, len(tbl) - 1)

print("Wypisanie iteracyjne:")
iteracja(tbl)