'''Instrukcje warunkowe ID: 05
Zadanie - listę wartości 'lista' należy rozdzielić
na trzy listy:
l1 zawiera elementy mniejsze równe niż v1
l2 zawiera el. wększe niż v1 i mniejsze niż v2
l3 zawiera elementy pozostałe'''

l1, l2, l3 = [], [], [] # podstawienie wielokrotne
v1 = 5
v2 = 12
lista = [12, 4, 1,-900, 5600, 12, 2, 4, 2.1, -740,
         -1200, 3400, 4500, 3, 2, 5.5, 6.5, 8.5]
indeks = 0
while indeks < len(lista):
    if lista[indeks] <= v1:
        l1.append(lista[indeks])
    elif lista[indeks] < v2:
        l2.append(lista[indeks])
    else:
        l3.append(lista[indeks])
    indeks += 1
else:
    print("a teraz pocałuj się w 'czapkę'")

print('',l1,'\n',l2,'\n',l3)
