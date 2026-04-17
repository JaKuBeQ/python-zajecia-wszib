'''TSD@2020 QuickSort'''

from random import randint
from time import time

A = [randint(1,10**6) for i in range(3*10**5)]
B = sorted(A.copy())

def QuickSort(tb):
    if len(tb) < 2 : return tb
    L,P = [],[]
    piv = tb[0]
    for itr in tb[1:] :
        if itr < piv :
            L.append(itr)
        else : P.append(itr)
    return QuickSort(L) +[piv]+ QuickSort(P)

t0 = time()
if QuickSort(A) == B : print(f"O.K. Czas \
sortowania {len(A)} liczb %7.5f" %(time()-t0))
