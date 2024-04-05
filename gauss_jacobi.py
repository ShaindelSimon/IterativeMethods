#Shain Simon
#Shira Chaim
import numpy as np
from numpy.linalg import inv, norm

def check_diag(mat):
    for i in range(len(mat)):
        abs_row = np.abs(mat[i])
        sum_row = np.sum(abs_row)
        abs_diag = np.abs(mat[i, i])
        if sum_row - abs_diag > abs_diag:
            raise Exception("this is not dominant diagonal matrix")

def iterative_method(G, H, b):
    e = 0.001
    X = np.matrix(np.zeros((len(G), 1)))

    while True:
        next_X = G * X + H * b
        delta = norm(next_X-X, np.inf)

        if delta < e:
            break

        X = next_X

    return X

def DLU(mat):
    D = np.matrix(np.diag(np.diag(mat)))
    L = np.tril(mat, -1)
    U = np.triu(mat, 1)
    return D, L, U
def Jacobi(mat, b):
    check_diag(mat)
    D, L, U = DLU(mat)
    H = inv(D)
    G = -H * (L+U)
    return iterative_method(G, H, b)
def Gauss_Z(mat, b):
    check_diag(mat)
    D, L, U = DLU(mat)
    H = inv(L+D)
    G = -H * U
    return iterative_method(G, H, b)





def main():
    mat = np.matrix([
        [ 2,  3,  4, 5, 6],
        [ -5, 3,  4, -2, 3],
        [ 4,  -5,  -2, 2, 6],
        [4, 5, -1, -2, -3],
        [5, 5, 3, -3, 5]
    ])
    b = np.matrix([[70], [20], [26], [-12], [37]])
    print(Jacobi(mat, b))
    #print(Gauss_Z(mat, b))


main()