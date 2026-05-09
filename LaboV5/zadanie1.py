'''
imie nazwisko: jakub łysiak
ID: 05
temat zadania - sortowanie bucket sort ułamków
'''

from time import time
from random import uniform

D = [uniform(0,1) for i_88 in range(10**6)]

B = len(D)//5

Buc = [[] for ir in range(B)]

def srt(A):
    G = []
    while A:
        ind = A.index(min(A))
        G.append(A.pop(ind))
    return G

for ir in D:
    hasH = int(ir*B)
    Buc[hasH].append(ir)

    K = []
    for ir in Buc:

