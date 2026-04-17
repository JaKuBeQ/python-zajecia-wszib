'''TSD@2020 MergeSort'''

from random import randint
from time import time

B = [randint(1,10**6) for i in range(3*10**5)]
C = sorted(B.copy())

def mergeSort(A,p,r) :
    if p >= r-1 : return A
    q = (p+r)//2
    mergeSort(A,p,q)
    mergeSort(A,q,r)
    return Merge(A,p,q,r)

from math import inf

def Merge(A,p,q,r) :
    L = A[p:q]+[inf] 
    R = A[q:r]+[inf]
    i,j = 0,0
    for k in range(p,r):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

t0 = time()

if C == mergeSort(B,0,len(B)) : print(f"O.K Czas\
 sortowania {len(B)} liczb: %7.5f" %(time()-t0))
