'''Przykład obliczania silni
porównanie: iteracja vs rekursja'''

import time

n = 900

# --- najpierw zwykła pętla for ---
def silnia_iter(n):
    wynik = 1
    for i in range(1, n+1):
        wynik = wynik * i
    return wynik

t1 = time.time()
w1 = silnia_iter(n)
t2 = time.time()

print("Silnia iteracyjnie:", w1)
print("Czas iteracja:", t2 - t1)


# --- teraz to samo z użyciem funkcji rekursywnej ---
def silnia_rec(n):
    if n == 0 or n == 1:
        return 1              # warunek stopu rekursji
    else:
        return n * silnia_rec(n-1)   # wywołanie samej siebie

t3 = time.time()
w2 = silnia_rec(n)
t4 = time.time()

print("Silnia rekursyjnie:", w2)
print("Czas rekursja:", t4 - t3)


# --- sprawdzenie zgodności ---
if w1 == w2:
    print("O.K.")