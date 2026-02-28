'''Rekursja
'''
#Silnia
def Silnia(n):
    if n == 1: return 1
    res = n * Silnia(n-1)
    return res

m = 5
d = Silnia(m)
print('Wartość funkcji silnia dla ',m,'  -  ',d)


#Suma elementów listy
def Suma(lista):
    if len(lista)==1: return lista[0]
    return lista[-1] + Suma(lista[:-1])

dane = [1,2,3,4,200,210]
somma = Suma(dane)
print('Dane = ', dane,' Suma danych = ', somma)
