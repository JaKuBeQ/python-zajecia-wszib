'''Pętla for .. in ..
Uwaga: po elementach wszystkich danych złożonych
w Python'ie można iterować.
for itr in "string"/[lista]/(entka,)/
{słownik:}/{zbiór}:
    dalej ...
'''
zest = ['Dom', 'Droga', 'Latarnia', 'Okno']

for element in zest:
    print(element)
    
licz = 0
while licz < len(zest):
    print('Indeks', licz, zest[licz])
    licz = licz + 1

#Suma wartości elementów listy
liczby = [12,12,14,1256,350]

suma=0
for element in liczby:
    suma = suma + element
print('Suma = ', suma)
print(sum(liczby))

#Silnia
val = 3
fact = 1
licz=1
while licz < val+1:
    fact = fact*licz
    licz = licz+1
print('Silnia(%i) =' % val ,fact)
