# ===== PROSTE SORTOWANIA + TABLICE =====
from random import randint
from time import time

# ===== GENEROWANIE TABLICY =====
def losowa(n, a=1, b=100):
    return [randint(a, b) for _ in range(n)]

# ===== SORTOWANIA =====

# 1. Selection Sort (wybieranie)
def selection_sort(T):
    for i in range(len(T)):
        mn = i
        for j in range(i, len(T)):
            if T[j] < T[mn]:
                mn = j
        T[i], T[mn] = T[mn], T[i]

# Złożoność: O(n^2)

# 2. Bubble Sort (bąbelkowe)
def bubble_sort(T):
    for i in range(len(T)):
        zamiana = False
        for j in range(1, len(T)-i):
            if T[j-1] > T[j]:
                T[j-1], T[j] = T[j], T[j-1]
                zamiana = True
        if not zamiana:
            break

# Złożoność: O(n^2), najlepszy przypadek O(n)

# 3. Insertion Sort (wstawianie)
def insertion_sort(T):
    for i in range(1, len(T)):
        x = T[i]
        j = i - 1
        while j >= 0 and T[j] > x:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = x

# Złożoność: O(n^2), najlepszy przypadek O(n)

# ===== OPERACJE NA TABLICACH =====

def minimum(T):
    return min(T)

def maksimum(T):
    return max(T)

def suma(T):
    return sum(T)

def srednia(T):
    return sum(T) / len(T)

def czy_posortowana(T):
    return all(T[i] <= T[i+1] for i in range(len(T)-1))

def odwroc(T):
    return T[::-1]

def kopiuj(T):
    return T.copy()

# ===== TEST =====
if __name__ == "__main__":
    A = losowa(10000, 1, 10000)
    B = sorted(A.copy())

    t0 = time()
    insertion_sort(A)

    if A == B:
        print("OK | czas:", round(time() - t0, 5))