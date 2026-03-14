'''TDy@2022 Przykłady pętli for..in..
Zadanie: wypisać kolejne imiona z listy koledzy
oraz ich indeksy - numery miejsca na liście  Jakub Łysiak id : 05 '''

koledzy=['Czarek','Kaziu','Grześ','Basia']

#bezpośrednie iterowanie po danych w postaci listy
i=0         
for tup in ['Czarek','Kaziu','Grześ','Basia']:
    print(i,tup)
    i+=1

print()     #druk pustej linii - odstęp

#iterowanie po elem. zmiennej, która jest listą
for tup in koledzy:
    print(koledzy.index(tup),tup) #metoda x.index()
print()

for no,imie in enumerate(['Czarek','Kaziu','Grześ','Basia']):
    print(no,imie)  #enumerate zwraca indeks i wart.
print()

#iterowanie po kolejnych wartościach indeksu
for i in range(len(koledzy)): #range(4) => (0,1,2,3)
    print(i,koledzy[i])
print()          

#       ***** ***** ***

#pętla "for" wbudowana w deklarację listy - 
#- operacja poprzedza "for"

B = ['Balbina'+i for i in 'Bolo']
print(B,'\n')       # oraz dodaj nową linię

#pętla "for" wbudowana w deklarację listy A - 
#- operacje zdefiniowane są jako funkcja

def kwadrat(x):     #definicja funkcji
    return x*x  

A = [kwadrat(i) for i in range(8) if i%2==0]
print(A)
