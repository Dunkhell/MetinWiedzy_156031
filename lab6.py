import math as m
import numpy as np


def matrix_cov(matrix):
    return np.dot(matrix.T, matrix)


def matrix_invertible(matrix):
    return np.linalg.inv(matrix)


def left_invertible(matrix):
    kow = matrix_cov(matrix)
    m_inv = matrix_invertible(kow)
    return np.dot(m_inv, matrix.T)


def linear_regression(matrix):
    matrix_x = np.array([[1, x[0]] for x in matrix])
    matrix_y = np.array([x[1] for x in matrix])
    lef_inv = left_invertible(matrix_x)
    return np.dot(lef_inv, matrix_y)


x_y = np.array([[2, 1], [5, 2], [7, 3], [8, 3]])
print(linear_regression(x_y))
