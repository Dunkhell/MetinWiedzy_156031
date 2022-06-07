from lab7 import qr_decomposition
import numpy as np


def matrix_k1(a):
    q = qr_decomposition(a)[0]
    new_a = np.dot((q.T, a), q)
    return new_a


def matrix_eigenvalues(a):
    new_a = a
    while (np.diag(new_a) - np.dot(new_a, np.ones((new_a.shape[0], 1))).T).all() > 0.01:
        new_a = matrix_k1(new_a)
    return np.diag(new_a)

