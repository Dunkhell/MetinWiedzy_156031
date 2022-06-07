import numpy as np
from lab7 import qr_decomposition
from lab9 import gauss
import sympy as sp

def matrix_k1(a):
    q = qr_decomposition(a)[0]
    new_a = np.dot(q.T, a)
    new_a = np.dot(new_a, q)
    return new_a


def matrix_eigenvalues(a):
    new_a = a
    while (np.diag(new_a) - np.dot(new_a, np.ones((len(new_a[0]), 1))).T).all() > 0.001:
        new_a = matrix_k1(new_a)
    return new_a


def calc_u(a):
    u = np.array(a.shape)
    aat = np.dot(a, a.T)
    lambdas = np.linalg.eigvals(aat)
    for lambda_i in lambdas:
        aat_copy = np.copy(aat)
        for i in range(aat_copy.shape[0]):
            for j in range(aat_copy.shape[1]):
                if i == j:
                    aat_copy[i][j] -= lambda_i

        zeros = np.zeros((aat_copy.shape[0], 1))
        aat_copy = np.concatenate((aat_copy, zeros), axis=1)

        u_i = gauss(aat_copy)
        print(u_i)


def svd(a: np.ndarray):
    m, n = a.shape
    calc_u(a)


matrix_in = np.array([
    [1, 2, 0],
    [2, 0, 2]
])
svd(matrix_in)
