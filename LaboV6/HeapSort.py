'''TDy@2020 Kopiec Heap użyty do sortowania'''

def downHeap(k,n):
    v = A[k]
    while k <= n//2:
        j = 2*k
        if j < n and A[j] < A[j+1]: j += 1
        if v >= A[j]: break
        A[k] = A[j]
        k = j
    A[k] = v

def delMax(n):
    dmax = A[1]
    A[1] = A[n]; n -= 1
    if n > 1 : downHeap(1,n)
    return dmax

def construct(A):
    for i in range((len(A)-1)//2, 0, -1):
        downHeap(i,len(A)-1)

import time
from random import randint

def losowa(ile, od, do):
    return [randint(od,do) for i in range(ile)]

ile = 2*10**5
tble1 = losowa(ile,1,10**6)
tble2 = sorted(tble1.copy())

#HeapSort
global A

A = ['A qq'] + tble1
t0 = time.time()
construct(A)

for i in range (len(A)-1,0,-1):
    A[i] = delMax(i)
del A[0]

print('\nSort. kopcowe %i liczb w czasie %5.3f'%(ile,
      time.time()-t0))
if A == tble2 :
    print('Sortowanie poprawne')
