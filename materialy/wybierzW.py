'''T.S.Dyduch @ 2019 Sortowanie przez wybieranie
"w miejscu" ok.10sec.
'''
from random import randint
from time import time

def dajListe(ile,od,do):
    return [randint(od,do) for i in range(ile)]

A=dajListe(4000,1,10000)
    
def mini(lista): #wyznacza wartość najmniejszą w liście
    mi,ind=lista[0],0
    for i in range(1, len(lista)):
        if mi>lista[i]:
            mi,ind=lista[i],i
    return ind

t0=time()
posort=[]
kopia = A+[]

for i in range(len(kopia)-1): #sortowanie 'w miejscu'
    mimo = i+mini(kopia[i:])
    kopia[i],kopia[mimo]=kopia[mimo],kopia[i]
'''    
#sortowanie 'nie w miejscu': 
while kopia:    #wybieramy kolejno z kopia do posort
    indo=mini(kopia)
    posort.append(kopia.pop(indo))
kopia=posort    #tylko dla zachowania zgodności
'''
kopia2=A+[]
kopia2.sort() #.sort jest metodą obiektów list
if kopia2==kopia: print('Sortowanie poprawne w czasie',
                         time()-t0)
else: print('Coś nie halo!')
