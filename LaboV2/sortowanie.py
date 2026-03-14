'''
imie naziwsko: jakub łysiak
ID: 05
temat zadania - sortowanie przez wybieranie
'''

from random import randint
from time import time

tbl = [randint(1,10**5) for i in range(10**4)]

tb2 = tbl.copy()
tb2.sort()

t0 = time()
tbsort = []

while tbl :
    ix = tbl.index(min(tbl))
    tbsort.append(tbl.pop(ix))
if tbsort == tb2 :
    print('ok czas sortowania: ', time() - t0)

