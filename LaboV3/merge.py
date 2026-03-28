'''
imie naziwsko: jakub łysiak
ID: 05
temat zadania - merge list jako funkcja (funkcja zaplatania)
'''

from random import randint
from math import inf

Tb1  = [randint(0, 100) for ix_88 in range(100)]
Tb2  = [randint(0, 100) for ix_88 in range(105)]

Tb1.sort(reverse=True)
Tb2.sort(); Tb2.reverse()

def merge(A,B):
    Splot = []
    L = len (A); l = 0
    R = len (B); r = 0
    while l < L and r < R:
        if A[l] >  B[r]:
            Splot.append(A[l])
            l += 1
        else:
            Splot.append(B[r])
            r += 1\

    Splot += A[l:] + B[r:]
    return Splot

def merge2(A,B):
    A.append(-inf)
    B.append(-inf)
    Splot = []
    L = len (A); l = 0
    R = len (B); r = 0
    while l + r < R+L-2:
        if A[l] >  B[r]:
            Splot.append(A[l])
            l += 1
        else:
            Splot.append(B[r])
            r += 1\

        #Splot += A[l:] + B[r:]
    return Splot

Odpow = merge(Tb1, Tb2)
print(Odpow)

Odpow2 = merge2(Tb1, Tb2)
print(Odpow2)