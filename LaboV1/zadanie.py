'''dobry wieczór z tej strony ID: 05 a to temat: Pierwiastkowanie metodą rolnika'''

Num  = float(input('wpisz liczbę dodatnią do spierwiastkowania: \n'))

if Num < 0: print('miała być dodatnia')

eps = 10**-6
a, b = 1, Num
while (a-b)**2 > eps:
    a = (a+b)/2
    b = Num/a

print('pierwiastek z podanej liczby %f wynosi %f: ' %(Num,a))