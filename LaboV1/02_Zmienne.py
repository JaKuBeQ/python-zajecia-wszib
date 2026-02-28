'''Dane liczbowe int 7, float 3.14, complex 5+2j
i złożone "str", [list], (tuple,), {dict:value}
i {set}. Stałe logiczne False / True
ID: 05
'''
print('ID: 05\n')
#Instrukcja podstawienia do zmiennej
alfa = 80
beta = 64.4
delta = True #wartość logiczna

print(80, 64.4, True)
print(alfa,   beta  ,delta)

alfa = alfa + 90
print('alfa = ', alfa)

alfa += 100  # notacja równoważna alfa = alfa+100
print('alfa = ', alfa)

print( alfa*5)

print('alfa/4 = ',alfa/4)

print(type(beta))
beta = (alfa + 3)**2 #typ zmiennej zależy od danej
print('beta = ',beta, type(beta))

t = 176453//177
print(t, 176453%177 )
