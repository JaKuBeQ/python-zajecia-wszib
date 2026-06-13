'''Algorytmy Bubble_Sort'''

import random, time

#Utworzenie sekwencji do sortowania
ile = 4000
tble1 = [random.randint(0,10**4) for i in range(ile)]
popr = tble1 +[]

#Sortowanie bąbelkowe
licz = 0
t0=time.time()

k=len(tble1)
swap=True
while swap :
    i=1
    k-= 1
    swap=False
    while i <= k :
        s=tble1[i-1]
        while i <= k and s > tble1[i] :
            tble1[i-1] = tble1[i]
            swap=True; licz += 1
            i+=1
        tble1[i-1]= s
        i+=1
            
t1=time.time()

#Sort. bąbelkowe2

licz1 = 0
t00 = time.time()

def Bubble_Sort(A,licz=0) :
    for i in range(len(A)-1) :
        for j in range(len(A)-1, i, -1) :
            if A[j] < A[j-1] :
                x= A[j]; A[j]= A[j-1]; A[j-1]=x
                licz+=1
    return(A,licz)

tble2=popr+[]
tble2,licz2 = Bubble_Sort(tble2)
t11 = time.time()

popr.sort()

if popr==tble1:
    
    print ("\nSortowanie bąbelkowe while.. ")
    print ("Liczba zamian ", licz)
    print('Czas :',t1-t0)

if popr==tble2:      
    print ("\nSortowanie bąbelkowe for..in.")
    print ("Liczba zamian ", licz2)
    print('Czas :',t11-t00)

