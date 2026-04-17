'''TSD@2020 MergeSort + licznik operacji i czas'''

from random import randint
from time import time
from math import inf

# --- generator listy ---
B = [randint(1, 10 ** 6) for i in range(3 * 10 ** 5)]
C = sorted(B.copy())

# --- licznik operacji ---
porownania = 0
przypisania = 0


# --- funkcja MergeSort ---
def mergeSort(A, p, r):
    if p >= r - 1: return A  # warunek stopu
    q = (p + r) // 2
    mergeSort(A, p, q)
    mergeSort(A, q, r)
    return Merge(A, p, q, r)


# --- scalanie ---
def Merge(A, p, q, r):
    global porownania, przypisania

    L = A[p:q] + [inf]
    R = A[q:r] + [inf]

    i, j = 0, 0

    for k in range(p, r):
        porownania += 1
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
            przypisania += 1
        else:
            A[k] = R[j]
            j += 1
            przypisania += 1
    return A


# --- pomiar czasu ---
t0 = time()

W = mergeSort(B, 0, len(B))

t1 = time()

# --- wyniki ---
if C == W:
    print("O.K.")
    print("Czas sortowania:", t1 - t0)
    print("Liczba porównań:", porownania)
    print("Liczba przypisań:", przypisania)
    print("Rozmiar danych:", len(B))