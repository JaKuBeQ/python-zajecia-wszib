'''TDy@2022 Dijkstra: przyłącz najbliższego
(zachłanny) i aktualizuj wartości jego sąsiadów.
Directed Valued Graph DVGr[i] =
= [[ojciec,value],[1syn,odl],[2syn,odl],...] 
'''
global Inf, DVGr 
global Solved, Qu, n
InF = 999

DVGr=[[[-1,0],[1,3],[4,3]],[[None,InF],[2,1],[0,3]],
      [[None,InF],[3,3],[5,1]],[[None,InF],[1,3]],
      [[None,InF],[5,3]],[[None,InF],[0,6],[3,1]]]

Solved = [-1,0]; Qu = [0]; n = 0
print(' Graf odległości - początkowy.')
print('[iD ojca, wartość],[iDsyna,odległość],[..')
for itm in DVGr:
    print(itm)

''' Priorytetowa kolejka węzłów Qu[ix] zrealizowana
alg. Heap. Priorytety węzłów ix to ich aktualne wartości
w=DVGr[Qu[ix]][0][1]. W kolejce stoją indeksy ix węzłów
'''
def prio(ix): return DVGr[Qu[ix]][0][1]

def upHeap(ix):
    vk = Qu[ix]
    w = prio(ix)
    q = ix//2
    while q > 0 and prio(q) > w :
        Qu[ix] = Qu[q]
        ix = q; q = q//2
    Qu[ix] = vk

def downHeap(ix,n):
    vk = Qu[ix]
    w = prio(ix)
    while ix <= n//2:
        j = 2*ix
        if j < n and prio(j) > prio(j+1):
            j += 1
        if w <= prio(j): break
        Qu[ix] = Qu[j]
        ix = j
    Qu[ix] = vk

def delMin():
    global n
    dmin = Qu[1]
    Qu[1] = Qu[n]; n -= 1 
    if n > 1 : downHeap(1,n)
    del Qu[n+1]
    return dmin

def val(node): return DVGr[node][0][1] #to tylko skrót

def Value (pa): #przelicz wartości potomnych
    global n
    for son in DVGr[pa]:
        sonID = son[0]
        if sonID not in Solved :
            if val(pa) + son[1] < val(sonID):
                DVGr[sonID][0][1] = val(pa) + son[1]
                DVGr[sonID][0][0] = pa
            if sonID not in Qu :
                Qu.append(sonID)
                n += 1; upHeap(n)
            else: upHeap(Qu.index(sonID))
    return 

def minNode():  #wybór najbliższego z kolejki
    Nmin = delMin()
    Solved.append(Nmin)
    return Nmin

Value(0)
while len(Qu) > 1:
    Value(minNode())

print('\n Graf rozwiązania - drzewo rozpinające.')
print('iD [iD ojca, najkrótsza odległość]')
n = 0
for itm in DVGr:
    print('',n,itm[0])
    n += 1
print()

cel = 1
while cel > 0:
    cel=int(input('Dokąd jedziemy? Podaj nr węzła:'))
    if cel < 0 or cel > len(DVGr)-1:
        print('Jedź sobie sam.');continue
    droga = [cel]; pa = DVGr[cel][0][0]
    while pa > 0:
        droga.insert(0,pa)
        pa = DVGr[pa][0][0]
    droga.insert(0,0)
    print(droga)
