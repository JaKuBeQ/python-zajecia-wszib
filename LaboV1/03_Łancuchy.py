'''Łańcuchy (string) ID: 05
'''
strg = 'Spisane będą czyny i rozmowy.'
print(strg)

#Numeracja elementów (indeksy) danej złożonej od 0
print(strg[5:20])
print()

#Wydzielenie części łańcucha
ds_17 = strg[:8]*3
print(ds_17)

#len - funkcja zwracająca długość łańcucha
print(len(strg))

#Sumowanie
wrs = '\nLepszy dla ciebie byłby świt zimowy.'
print (strg + wrs)
Wersy = strg + wrs

#string jest obiektem Ma 49 metod: str.metoda(arg)
print(Wersy.split())

# Nie można zmienić zawartości łańcucha np.
# strg[4]='k'.
