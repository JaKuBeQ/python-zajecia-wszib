'''TSD@2021 Algorytm Hoare znajdowania n-tego co do
wartości elementu danej listy bez sortowania'''

from random import randint
from time import time

test = [randint(1,10**6) for i in range(5*10**5)]
med = len(test)//2

def dziel(tb):
    piv = tb[0]
    L = []; P = []
    for itr in tb[1:] :
        if itr < piv :
            L.append(itr)
        else: P.append(itr)
    return len(L), L +[piv] +P

def Hoare(tb,znajdz):    
    iL, tb = dziel(tb)
    p = 0; licz = 1
    while p+iL != znajdz:
        if p+iL < znajdz:
            tb = tb[iL+1:]
            p += iL+1
        elif p+iL > znajdz :
            tb = tb[:iL]
        iL, tb = dziel(tb)
        licz += 1
    return tb[iL],licz

t0 = time()
medi,count = Hoare(test, med)
print(f"Mediana: {medi} Ilość podziałów: {count}")
print(f"Ilość danych: {len(test)} \
Czas: %7.5f" % (time()-t0)) 
'''
test = [23, 4, 33, 9, 11, 74, 9, 33]
znajdz=1
while znajdz:
    print(test)
    znajdz = int(input('Którą w kolejności znaleźć? '))
    if znajdz < 0 or znajdz >= len(test): continue
    seat,ble = Hoare(test,znajdz)
    print(f"To jest {seat}.\n")
'''
