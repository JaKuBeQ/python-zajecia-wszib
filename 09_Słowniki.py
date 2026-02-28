'''Słownik - Tablica asocjacyjna
'''
telefony ={'Karol':'+48 22 777773',
           "Paweł":"+48 12 4227492",
           'Jan':"+48 22 6554555"}
telefony["Ela"] = "+39 8763655"

#Drukowanie całego słownika
print(telefony)

#Drukowanie wybranej pozycji słownika
imie = 'Paweł'
print(imie, telefony[imie])

#Odszukanie osoby która ma określony nr telefonu
for osoba in telefony:
    if telefony[osoba] == "+48 22 6554555" :
        print(osoba,telefony[osoba])

'''WAŻNE: iterator w przypadku danej typu dict
iteruje tylko po kluczach - równoważnie:
for osoba in telefony.keys():
    if telefony[osoba] == ...

Przynależność do elementów słownika też odnoszona
jest tylko do zbioru kluczy.
'''
if 'Ela' in telefony: print('Ela',telefony['Ela'])

print(telefony.keys())
numery=list(telefony.values())
print(numery)

#połączenie listy ze słownikami atrybutów
spis=[{'co':'kiwi','jm':'szt','cena':3.50,'ile':30},
      {'co':'kaka','jm':'kg','cena':24.0,'ile':6.30}]

for coś in spis:
    print(f"{coś['co']} -\
 jest warte {coś['cena']*coś['ile']}")
