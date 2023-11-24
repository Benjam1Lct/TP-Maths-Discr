import numpy as np

def diagonale(A):
    B = np.copy(A)
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i != j:
                B[i, j] = 0

    return B

def transpose(A):
    B = np.copy(A)
    for i in range(len(A)) :
        for j in range(len(A[i])):
            B[j, i] = A[i, j]
    return B

def produit (A, B):
    C=np.zeros(np.array(np.shape(A)[1], np.shape(B)[0]))
    result = 0
    if np.shape(A)[1] != np.shape(B)[0]:
        return []
    for i in range(len(A)):
        result = 0
        for j in range(len(B)):
            result += A[i][j] + B[j][i]
        C[i][j] = result
    return C



if __name__ == '__main__':
    A = np.array([[1, 2, 3], [4,5,6], [7,8,9],[2,8,4]])
    B = np.array([[1, 2, 3], [4,5,6], [7,8,9]])
    
    B = diagonale(A)
    C = transpose(A)
    D = produit(A,B)
    print(D)