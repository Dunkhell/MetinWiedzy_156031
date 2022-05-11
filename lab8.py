from lab7 import qr_decomposition
import numpy as np


def matrix_k1(a):
    q = qr_decomposition(a)[0]
    new_a = np.dot(q.T, a)
    new_a = np.dot(new_a, q)
    # if k > 1 :
    #    return matrix_eigenvalues(new_a, k-1)
    return new_a


def matrix_eigenvalues(a):
    new_a = a
    i = 0
    while (np.diag(new_a) - np.dot(new_a, np.ones((5, 1))).T).all() > 0.01:
        new_a = matrix_k1(new_a)
        i = i + 1
        print(f'step {i} -> \n{(np.diag(new_a) - np.dot(new_a, np.ones((5, 1))).T).all()}')
    return np.diag(new_a)


a = np.array(
    [[1., 2., 3., 4., 5.], [2., 2., 3., 4., 5.], [3., 3., 3., 4., 5.], [4., 4., 4., 4., 5.], [5., 5., 5., 5., 5.]])
# wartosci wlasne wedlug kalkulatora online
# λ_1≈19,598
# λ_2≈-3,185
# λ_3≈-0,750
# λ_4≈-0,386
# λ_5≈-0,277

print(a)
wynik = matrix_eigenvalues(a)
print("================ WYNIK ================", np.round(wynik, decimals=3), sep="\n")
