'''04 [Listy] i (entki,)
'''
lista = ['jabłko', 'gruszka', 'śliwka', 'morela',
         'mango']
entka = tuple(lista)

#Numeracja indeksu od 0
print(lista,'\n',entka)

print('\n',lista[2:4],'\n',entka[:3])

'''Wymiana elementu listy
UWAGA: w entce to i następne są niemożliwe!'''
lista [2] = 'cytryna'
print('\n',lista)

#Dołączenie elementu do listy na jej końcu -
# metoda 'append'
lista.append('orzech')
print('\n',lista)

#Dołączenie innej listy na koniec listy -
# metoda 'extend'
lista.extend(['figa', 'kaka'])
print('\n',lista)

#Umieszczenie elementu w określonej pozycji listy -
# metoda 'insert'
lista.insert(3,'czereśnia')
print('\n',lista)

#Usunięcie fragmentu z listy
del lista[4:6]
print('\n',lista)

#Lista jako stos
iD_99=lista.pop()
print('\n',iD_99, lista)

lista.reverse()
print('\n',lista)

#Możlie jest arytmetyczne dodawanie w obu typach
print([7,12]+[3,4],'\n',(7,12)+(3,4))
