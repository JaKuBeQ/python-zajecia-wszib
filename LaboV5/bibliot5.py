'''biblioteka'''

def radixSort(A,t,k=10) :
    #Puste liczniki
    C = [0]*k
    #Zliczamy wystąpienia liczb
    for j in range(len(A)) :
        C[int(A[j][t])] += 1
    #Liczniki będą zawierać liczbę poprzedników
    for i in range(1,k) :
        C[i] = C[i] +C[i-1]
    #Składamy elementy A od tyłu, wg C, w ciąg
    # posortowany B, aktualizując C
    B = A +[]
    for j in range(len(A)-1,-1,-1) :
        B[C[int(A[j][t])]-1] = A[j]
        C[int(A[j][t])] -= 1
    return B
