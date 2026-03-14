'''TDy@2019 sortowanie przez wstawianie insSort
5k danych ok.2 sec.  Jakub Łysiak id : 05 '''

import time
from random import randint

a, b, c = 1, 5000, 10000
i =0 ; A =[]
#losowanie listy do posortowania
while i<b :
    A.append(randint(a,c))
    i += 1

B=A+[]
licz_33 = 0
t0=time.time()

for j in range(1,len(A)):
    key = A[j]
    i = j-1
    while i>=0 and A[i]>key :
        A[i+1] = A[i]
        i -= 1
        licz_33 += 1
    A[i+1] = key
      
print ("\nSortowanie przez wstawianie")
print ("Liczba kroków-przesunięć ", licz_33)
print('Czas :',time.time()-t0)
B.sort()
if A==B: print('To działa.')
