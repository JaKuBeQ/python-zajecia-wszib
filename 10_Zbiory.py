'''Zbiory (set) i entki (tuple) w Python'ie
Uwaga: po elementach wszystkich danych złożonych
w Python'ie można iterować.
for itr in string/lista/entka/słownik/zbiór:
    dalej ...
'''
a=set([1,2,3])
print('Zapis zbioru:',a)
b=(3.14,)
print('Zapis entki z jednym elementem:',b)
print('Entka przekszt. z listy:',tuple([1,2,3]))
c={2,3,4,5}
print(a&c)
print(a|c)
print(c-a)
'''pusta entka'''
f=()
print('Pusta entka:',f)
print('Suma entek:',f+('kicha',17))
'''zbiór pusty'''
d={()}
print(d&a)
e=set()
print('Zbiór pusty:',e)
