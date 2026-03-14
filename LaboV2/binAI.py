'''I N id_67 Odgadywanie liczby naturalnej<100'''

a, b = 1, 99
print('AI: Pomyśl liczbę naturalną < 100, a ja ją odgadnę.',
      '\nPodam Ci liczbę, a Ty odpowiedz kodem:',
      '\nza dużo - 3; za mało - 1; zgadłem - 2')

res = int(input(str(c)+' > '))
while res not in (1,2,3):
    res = int(input('? >'))
