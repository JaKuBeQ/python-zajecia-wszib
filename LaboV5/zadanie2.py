'''
imie nazwisko: jakub łysiak
ID: 05
temat zadania - couting sort liczb calkowitych
'''

from random import randint
from time import time

D = [randint(0,10**6-1) for i_88 in range(10**6)]

def CSrt(A, k):
    L = [0]*k
    for ir in A:
        L[ir] +=1
    As = []
    for i in range(len(L)):
        As.extend([i]*L[i])
    return As

D2 = sorted(D.copy())
T0 = time()
Ds = CSrt(D, 10**6)
if Ds == D2:
    print(f"spoko działa fajnie a czas wykonania wynosi:  {round(time() - T0,5)} sekundy")

