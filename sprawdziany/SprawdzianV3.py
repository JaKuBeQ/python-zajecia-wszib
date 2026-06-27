'''
imie nazwisko: jakub łysiak
ID: 05
temat zadania - wyznaczanie częstotliwości występowania najczęstszej pary znaków w podanym zdaniu
'''

tekst = "Miała mama mamałygę, ale mała ją zmęła i już jej nie ma."

licznik_par = {}

for i in range(len(tekst) - 1):
    pary = tekst[i:i+2] #tworzenie pary bieżącego znaku i kolejnego
    if pary in licznik_par:
        licznik_par[pary] += 1
    else:
        licznik_par[pary] = 1

najczestsze = None
max_licznik = 0

for pary, licznik in licznik_par.items():
    if licznik > max_licznik:
        najczestsze = pary
        max_licznik = licznik

print(f"Najczęściej występująca para: '{najczestsze}' wystąpiła {max_licznik} razy.")

# Złożoność tego kodu to O(n), ponieważ tekst jest przetwarzany liniowo, a operacje na słowniku są O(1).

