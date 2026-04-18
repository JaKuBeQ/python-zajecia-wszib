'''
imie naziwsko: jakub łysiak
ID: 05
temat zadania - program, sortujący zadaną listę metodą wybierania 'w miejscu'
'''

A = [23,32,2,3,45,32,12,21,11,7,77,17,39]


def wybIn(A):
    for i in range(len(A)):
        mn = i
        for j in range(i,len(A)):
            if A[j] < A[mn] : mn = j
        A[i], A[mn] = A[mn], A[i]
    return A

print("lista przed sortowaniem: ", A)
print("lista po sortowaniu: ", wybIn(A))

C = sorted(A.copy())
if C == wybIn(A):
    print("lista A zgadza się z posortowana lista A")



