'''
imie nazwisko: jakub łysiak
ID: 05
temat zadania - kodowanie huffmana
'''
from statistics import kde_random

tekst = 'Jeszcze jeden mazur dzisiaj, choć poranek świta.'
print('Tekst do kodowania: ', tekst)

global A
B = {'d':1,'u':8,'m':2,'a':4,'n':2,'k':1,'o':2}
B = {}
for lt in tekst:
    if lt in B:
        B[lt] += 1
    else:
        B[lt] = 1

A = {}; Qu = []

def sorQu(Qu,key):
    Qu.append(key)
    i = len(Qu)-2
    while i >= 0 and A[key][0] < A[Qu[i]][0]:
        Qu[i+1] = Qu[i]
        i -= 1
    Qu[i+1] = key

for i in B:
    A[i] = [B[i],None,None]
    sorQu(Qu,i)

while len(Qu) > 1:
    key1 = Qu.pop(0)
    key2 = Qu.pop(0)
    A[key1+key2] = [A[key1][0]+A[key2][0],key1,key2]
    sorQu(Qu,key1+key2)

root = Qu[0]
    
print('Drzewo Huffmana zakodowane w słowniku:\n', A)
print('\nKorzeń drzewa: ',root, A[root],'\n')

def HGraphVal(key):
    LS = A[key][1]
    if LS :
        A[LS][0] = A[key][0]+'1'
        HGraphVal(LS)
    RS = A[key][2]
    if RS :
        A[RS][0] = A[key][0]+'0'
        HGraphVal(RS)

A[root][0] = ''
HGraphVal(root)

print('Kody Huffmana alfabetu: \nlitera częstość kod Huffmana')
for i in B: print('%3s %7s %11s' %(i, B[i], A[i][0]))

# pisanie koderu

kdr = {}
for lt in B:
    kdr[lt] = A[lt][0]

KOD = ""
for lt in tekst:
    KOD += kdr[lt]
print(KOD)

rdk = {}
for lt in kdr:
    rdk[kdr[lt]] = lt

DECODED = ""
buf = ""
for bit in KOD:
    buf += bit
    if buf in rdk:
        DECODED += rdk[buf]
        buf = ""

print(DECODED)







