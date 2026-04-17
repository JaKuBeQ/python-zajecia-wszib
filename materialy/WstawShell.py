'''TSD@2018 Porównanie sortowania przez
wstawianie z ShellSort - szybszą wersją
'''
from random import randint
import time

def dajListe(ile, od, do):
    return [randint(od, do) for i in range(ile)]

ile = 5000
B = dajListe(ile,1,10000)
C = B.copy()

#Zwykłe sortowanie przez wstawianie
def Wstaw(A,h=1,licz=0) :
    for j in range(h,len(A)):
        key = A[j]
        i = j
        while i >= h and A[i-h] > key :
            A[i] = A[i-h]
            i -= h
            licz += 1
        A[i] = key
    return A,licz

t0 = time.time()
sB,licz1 = Wstaw(B)

print(f"Sort. przez wstawianie {ile} liczb\nLiczba\
 przesunięć {licz1} Czas %7.5f" %(time.time()-t0))

def Shellsort(A, krok, licz=0) :
    for k in range (len(krok)) :
        h = krok[k]
        A,licz = Wstaw(A,h,licz)
    return A,licz

'''wzór D.Knuth'a - historyczna ciekawostka
krok=[1]; i=1
while i < (ile//3) :
    i=i*3+1
    krok.append(i)
krok.reverse()
print(krok)
'''
krok=[1391376,463792,198768,86961,33936,13776,4592,
      1968, 861, 336, 112, 48, 21, 7, 3, 1 ]   

t0 = time.time()
sC,licz2 = Shellsort(C,krok)

print('Czas obliczeń Shellsort        %7.5f'\
      %(time.time()-t0))
print('Liczba przesunięć ',licz2)
if sC == sB : print('Oba sortowania są zgodne')
