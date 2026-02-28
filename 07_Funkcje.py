'''Funkcja Kalk - oblicza dla listy wartości sumę
oraz iloczyn elementów'''

def Kalk(lista):
    suma = 0
    iloczyn = 1
    for itm in lista:
        suma += itm
        iloczyn *= itm
    return suma, iloczyn
        
    
wartosci=[1,2,3,4]; print(wartosci)
suma, iloczyn = Kalk(wartosci)
print('Suma listy ',suma,'Iloczyn ',iloczyn)


'''Funkcja oblicza dla dwu wektorów iloczyn skalarny
oraz ich sumę'''

def Wekt(v1,v2):
    suma=[]
    iloczyn = 0
    for k in range(len(v1)):
        suma_cz = v1[k] + v2[k]
        suma.append(suma_cz)
        iloczyn += v1[k] * v2[k]
    return suma, iloczyn
    
w1 = [1,1,80,78]
w2 = [1,-1,-89,90]
print(w1,w2)

suma_wektorow, iloczyn_skalarny = Wekt(w1,w2)
print ('Suma wektorów = ', suma_wektorow,
       '\nIloczyn skalarny wektorów =',
       iloczyn_skalarny)
