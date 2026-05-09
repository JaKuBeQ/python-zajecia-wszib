'''
imie naziwsko: jakub łysiak
ID: 05
temat zadania - merge sort
'''

from random import randint
from time import time
from math import inf

A = [randint(0,10**6) for i_05 in range(10**6)]

B = sorted(A.copy())

def Msort(tab):
    if len(tab) < 2:
        return tab
    pv = len(tab)//2
    L = Msort(tab[:pv]) + [inf]
    R = Msort(tab[pv:]) + [inf]
    i, j = 0,0

    for k in range(len(tab)):
        if R[j] < L[i]:
            tab[k] = R[j]
            j +=1
        else:
            tab[k] = L[i]
            i += 1
    return tab
t0 = time()
ASort = Msort(A)
if ASort == B:
    print(f"lista jest posortowana i jej czas sortowania wynosi: {round(time()-t0,5)}")
else:
    print("lista źle posortowana")
