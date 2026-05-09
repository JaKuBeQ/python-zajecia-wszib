'''TDy@2022 Algorytm sortowania przez wstaw.'''

from random import randint
from time import time

k = 10000
A = [randint(0,k) for i in range(k)]
B = A + []

def karty(C):
    if len(C) < 2 : return C
    for i in range(1,len(C)):
        key = C[i]; j = i-1
        while j >= 0 and C[j] > key:
            C[j+1] = C[j]; j -= 1 
        C[j+1] = key
    return C

t0 = time()
A = karty(A)
print('Czas sortowania %i kart:' % k,time()-t0)
B.sort()
if A == B: print('O.k. Sortowanie poprawne.')
