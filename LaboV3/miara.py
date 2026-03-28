'''
imie naziwsko: jakub łysiak
ID: 05
temat zadania - Miara podobieństwa wektorów
'''
from random import randint
from math import sqrt

W1 = [randint(-10,10) for ix_88 in range(10)]
W2 = [randint(-10,10) for ix_88 in range(10)]

dW1, dW2, ilSk = 0,0,0
for ix in range(len(W1)):
    dW1 += W1[ix]**2
    dW2 += W2[ix]**2
    ilSk += W1[ix]*W2[ix]

cosW1W2 = ilSk/sqrt(dW1 * dW2)

print(f"Wektor W1 : {W1}\nWektor W2 : {W2}\ncosinus(W1-W2) : {cosW1W2: .2f}")