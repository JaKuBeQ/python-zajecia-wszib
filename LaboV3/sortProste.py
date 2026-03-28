'''Procedury sortowania proste Jakub Łysiak id : 05'''

from random import randint
from time import time

def wybIn(B):
    for i in range(len(B)):
        mn = i
        for j in range(i,len(B)):
            if B[j] < B[mn] : mn = j
        B[i], B[mn] = B[mn], B[i]

def bubble(B):
    for i in range(len(B)):
        flag = False
        for j in range(1,len(B)-i):
            if B[j-1] > B[j]:
                B[j-1], B[j] = B[j], B[j-1]
                flag = True
        if not flag: break

def wstaw(B):
    for i in range(1,len(B)):
        mv = B[i]; j = i-1
        while j >= 0 and B[j] > mv :
            B[j+1] = B[j]
            j -= 1
        B[j+1] = mv

A = [randint(1,10000) for i in range(10000)]
C = sorted(A.copy())

t0 = time()
wybIn(A)

if A == C :
    print("Jest O.K. "+
          "Czas obliczeń %7.5f" %(time()-t0))
