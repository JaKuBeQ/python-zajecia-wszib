''' Przykład tematu egzaminu praktycznego.
Uzupełnij kod procedury organizujacej kolejkę
priorytetową priQu i przeanalizuj złożoność
całego programu. Użyj zmiennej z Twoim Id
'''

global A
B={'d':1,'u':8,'m':2,'a':4,'n':2,'k':1,'o':2}

A={}; Qu=[]

def priQu(Qu,key):
    #procedura ma wstawić klucz "key" słownika A
    #do ciągu kluczy Qu posortowanego według A[key][0] 


for lt in B:
    A[lt]=[B[lt],None,None]
    priQu(Qu,lt)

while len(Qu)>1:
    k1=Qu.pop(0)
    k2=Qu.pop(0)
    A[k1+k2]=[A[k1][0]+A[k2][0],k1,k2]
    priQu(Qu,k1+k2)

print('Drzewo binarne zakodowane w słowniku:\n', A)
