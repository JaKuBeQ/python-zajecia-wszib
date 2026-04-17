'''@TDyduch 2020 Przykład definicji funkcji
i użycia rekursji
Dana jest lista liczbowa C. Wyznacz listę
sum częściowych, liczonych od początku C'''

C=[2,0,0,1,3,1,1,1,0,1]; C2=C.copy()

#najpierw zwykła pętla for
for i in range (1,len(C)):
    C[i]=C[i]+C[i-1]
print(C2)
print(C)

#teraz to samo z użyciem funkcji rekursywnej
def funRec(L,i):
    if i==0: return L   #warunek stopu rekursji
    else :
        funRec(L,i-1)   #wywołanie samej siebie
        L[i]=L[i]+L[i-1]
    return L
C1=funRec(C2,len(C2)-1)
print(C1)

if C1==C: print('O.K.') #potwierdzenie zgodności
