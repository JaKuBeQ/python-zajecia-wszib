'''Algorytm Hoare znajdowania n-tego co do wartości
elementu danej listy bez sortowania'''

test = [23, 4, 33, 11, 74, 9, 33]

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
    p = 0
    while p+iL != znajdz:
        if p+iL < znajdz:
            tb = tb[iL+1:]
            p += iL+1
        elif p+iL > znajdz :
            tb = tb[:iL]
        iL, tb = dziel(tb)
    return tb[iL]

znajdz=1
while znajdz:
    print(test)
    znajdz = int(input('ktorą w kolejności mam znalezc?'))
    if znajdz<0 or znajdz>=len(test): continue
    seat = Hoare(test,znajdz)
    print('To jest', seat)
