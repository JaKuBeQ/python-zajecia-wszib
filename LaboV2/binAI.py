'''Jakub Łysiak id : 05 Odgadywanie liczby naturalnej<100 '''

a, b, c = 1, 99, 50
print('AI: Pomyśl liczbę naturalną < 100, a ja ją odgadnę.',
      '\nPodam Ci liczbę, a Ty odpowiedz kodem:',
      '\nza dużo - 3; za mało - 1; zgadłem - 2')
      
res = int(input(str(c)+' > '))
while res not in (1,2,3):
    res = int(input('? >'))
while res !=2 and a <= b :
    if res == 1 :
        a = c + 1
    else :
        b = c-1
    c = (a + b) // 2
    res = int(input(str(c) + ' > '))

if res == 2 :
    print('Szukana liczba to ', c)
else :
    print('tak sie nie da')


