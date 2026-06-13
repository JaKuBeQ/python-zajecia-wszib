'''
imie nazwisko: jakub łysiak
ID: 05
temat zadania - funkcja rekursyjna, zamieniajacą zapis liczby z systemu dziesiętnego na dwójkowy.
'''

def convert(n):
    if n < 2:
        return str(n)
    return convert(n//2) + str(n%2)

def convert2(n):
    if n < 2:
        return str(n)
    return convert2(n//8) + str(n%8)



print("1024 w systemie dwojkowym  to ", convert(1024))
print("729 w systemie osemkowym to ", convert2(729))
