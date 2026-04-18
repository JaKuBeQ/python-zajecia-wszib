'''
imie naziwsko: jakub łysiak
ID: 05
temat zadania - quick sort
'''

from random import randint
from time import time

A = [randint(0,10**6) for i_05 in range(10**6)]

B = sorted(A.copy())

def Qsort(tab):
    if len(tab) < 2: return tab
    L, R = [], []
    piv = tab[0]
    for itm in tab[1:]:
        if itm>piv:
            R.append(itm)
        else:
            L.append(itm)
    return Qsort(L) + [piv] + Qsort(R)

t0 = time()
ASort = Qsort(A)
if ASort == B:
    print(f"lista jest posortowana i jej czas sortowania wynosi: {round(time()-t0,5)}")
else:
    print("lista źle posortowana")
