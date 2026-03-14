'''Wyszukiwanie binarne'''

Tb = [2,5,7,7,11,23,55,176,400]

print(Tb)
quest = int(input('Wpisz szukaną liczbę. >>'))
a, b = 0, len(Tb)-1

while b >= a:
    c = (a + b)//2
    if Tb[c] > quest:
        b = c -1
    elif Tb[c] < quest:
        a = c + 1
    else:
        print("Szukana liczba ma indeks %i" %c)
        break
else: print("Nie ma takiej liczby w liście")
