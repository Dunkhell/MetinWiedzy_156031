import numpy as np
from lab7 import qr_decomposition
import sympy as sp
import math


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


def gauss_reduction(matrix: np.ndarray):
    column_len = matrix.shape[0]
    result = []

    for y in range(column_len - 1):
        for x in range(column_len - 1):
            if y + x >= column_len - 1:
                continue
            times = matrix[x + 1 + y][y] / matrix[y][y]
            matrix[x + 1 + y] = matrix[x + 1 + y] - matrix[y] * times

            done = True
            for z in range(column_len - 1):
                if matrix[column_len - 1][z] != 0:
                    done = False

            if done is True:
                for k in range(column_len * 2 - 1, column_len - 1, -1):
                    result.append(matrix[column_len - 1][k])
                return result[::-1]

        for x in range(1, column_len):
            if y + x > column_len - 1:
                continue
            times = matrix[y][x + y] / matrix[x + y][x + y]
            matrix[y] = matrix[y] - matrix[x + y] * times

    return [matrix[i][column_len] / matrix[i][i] for i in range(column_len)]


def calc_u(a):
    u = []
    aat = np.dot(a, a.T)
    lambdas = np.around(np.linalg.eigvals(aat), decimals=1)
    lambdas[::-1].sort()
    for lambda_i in lambdas:
        aat_copy = np.copy(aat)
        for i in range(aat_copy.shape[0]):
            for j in range(aat_copy.shape[1]):
                if i == j:
                    aat_copy[i][j] -= lambda_i

        np_eye = np.eye(aat_copy.shape[0])
        aat_copy = np.concatenate((aat_copy, np_eye), axis=1)
        u_i = np.array(gauss_reduction(aat_copy))
        u_i = u_i / np.sqrt(np.sum(u_i ** 2))
        u.append(u_i.T)
    return np.array(u), lambdas


def calc_v(a):
    v = []
    ata = np.dot(a.T, a)
    lambdas = np.around(np.linalg.eigvals(ata), decimals=1)
    lambdas[::-1].sort()
    for lambda_i in lambdas:
        ata_copy = np.copy(ata)
        for i in range(ata_copy.shape[0]):
            for j in range(ata_copy.shape[1]):
                if i == j:
                    ata_copy[i][j] -= lambda_i

        np_eye = np.eye(ata_copy.shape[0])
        ata_copy = np.concatenate((ata_copy, np_eye), axis=1)
        v_i = np.array(gauss_reduction(ata_copy))
        v_i = v_i / np.sqrt(np.sum(v_i ** 2))
        v.append(v_i.T)
    return np.array(v)


def svd(a: np.ndarray):
    m, n = a.shape
    u, lambdas = calc_u(a)
    print(f'\nU MATRIX:\n{u}')
    v = calc_v(a)
    print(f'\nV MATRIX:\n{v}')
    singular_matrix = np.zeros((m, n))
    for i in range(singular_matrix.shape[0]):
        singular_matrix[i][i] = math.sqrt(lambdas[i])
    print(f'\nSINGULAR MATRIX:\n{singular_matrix}\n')

    print(np.around(np.dot(np.dot(u, singular_matrix), v), decimals=0))


matrix_in = np.array([
    [1, 2, 0],
    [2, 0, 2]
])

svd(matrix_in)
# Wszystko działa tylko w złym miejscu znaki wstawia :(