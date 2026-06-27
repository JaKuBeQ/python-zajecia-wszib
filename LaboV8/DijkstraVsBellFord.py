''' TDy@2022  Dijkstra: przyłącz najbliższego
(zachłanny) i aktualizuj jego sąsiadów. Directed Valued Graph
DGr[i]=[[ojciec,value],[1syn,odl],[2syn,...] '''

global Inf, DGr 
global Solved, Queue
Inf = 999

DGr = [[[-1,0],[1,3],[4,3]],[[None,Inf],[2,1],[0,3]],
       [[None,Inf],[3,3],[5,1]],[[None,Inf],[1,3]],
       [[None,Inf],[5,3]],[[None,Inf],[0,6],[3,1]]]

i = 0; print('Id  Węzły grafu połączeń')
for n in DGr:
    print(i, n); i += 1

Solved = [-1,0]; Queue = []

def vaL(n): return DGr[n][0][1]

def Value (pa):
    for son in DGr[pa]:
        sonID = son[0]
        if sonID not in Solved :
            if vaL(pa) + son[1] < vaL(sonID):
                DGr[sonID][0][1] = vaL(pa)+son[1]
                DGr[sonID][0][0] = pa
            if sonID not in Queue :
                Queue.append(sonID)
    return 

#kolejka priorytetowa nieuporządkowana
def minNode():
    miN = Inf
    for n in Queue:
        if vaL(n) < miN:
            miN = vaL(n)
            nmin = n
    Solved.append(nmin)
    Queue.remove(nmin)
    return nmin

Value(0)
while len(Queue)>0:
    Value(minNode())

#Rozwiązanie - minimalny graf rozpinajacy
i = 0; print('Id  Rozwiązanie')
for n in DGr:
    print(i, n[0]); i += 1
print()

def trasa(graf):
    cel = 1
    while cel > 0:
        cel = int(input('Dokąd jedziemy? Podaj nr węzła:'))
        droga = [cel]; pa = graf[cel][0][0]
        while pa > 0:
            droga.insert(0,pa)
            pa = graf[pa][0][0]
        droga.insert(0,0)
        print(droga)

'''Bellman-Ford Przeglądaj wszystkie węzły i poprawiaj
ich wartości, dopóki nie przestaną się zmieniać'''

BGr=[[[-1,0],[1,5]],[[None,Inf],[3,3],[4,9]],
     [[None,Inf],[0,3],[1,-4]],[[None,Inf],[4,3],[5,2]],
     [[None,Inf],[2,-1],[5,-5]],[[None,Inf],[0,9],[2,8]]]

i = 0; print('Id  Węzły grafu połączeń')
for n in BGr:
    print(i, n); i += 1

def BellFo(BGr):
    nx= - 1; loo = 0; chng = True
    for i in range(len(BGr)):
        nx += len(BGr[i]) - 1
    while loo < nx and chng:
        loo += 1; chng = False
        for i in range(len(BGr)):
            if BGr[i][0][0] != None:
                for j in range(1,len(BGr[i])):
                    rel = BGr[i][0][1]+BGr[i][j][1]
                    son = BGr[i][j][0]
                    if BGr[son][0][1] > rel:
                        BGr[son][0][1] = rel
                        BGr[son][0][0] = i
                        chng = True
    return chng

zle = BellFo(BGr)
if zle: print('Błędne dane!')
else:
    #Rozwiązanie - minimalny graf rozpinajacy
    i = 0; print('Id  Rozwiązanie')
    for n in BGr:
        print(i, n[0]); i += 1
