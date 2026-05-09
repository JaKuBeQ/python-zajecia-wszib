'''
imie nazwisko: jakub łysiak
ID: 05
temat zadania - sortowanie bucket sort ułamków
'''

from time import time
from random import uniform

D = [uniform(0, 1) for _ in range(10**6)]

B = len(D) // 5

Buc = [[] for ir in range(B)]

def srt(A):
    G = []
    while A:
        ind = A.index(min(A))
        G.append(A.pop(ind))
    return G

def Bsort(D, B):
    for ir in D:
        hasH = int(ir * B)
        if hasH >= B:
            hasH = B - 1
        Buc[hasH].append(ir)

    K = []
    for bucket in Buc:
        K.extend(srt(bucket))

    return K

D2 = sorted(D.copy())

t0 = time()
Ks = Bsort(D, B)

if Ks == D2:
    print(f"Działa! Czas wykonania wynosi: {round(time() - t0,6)} sekundy")
