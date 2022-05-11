import numpy as np
import math


def projection(u, a):
    division_higher = np.dot(u.T, a)
    division_lower = np.dot(u.T, u)
    if division_lower == 0:
        return u
    return np.multiply(u, division_higher / division_lower)


def matrix_len(a):
    result = math.sqrt(np.dot(a.T, a))
    return result if result != 0 else 1


def qr_decomposition(a):
    number_of_steps = len(a[0])
    vectors = []
    v_length = len(a)

    for x in range(number_of_steps):
        vector_n = []
        for i in range(v_length):
            vector_n.append(a[i][x])
        vectors.append(vector_n)

    u_vectors = []
    e_vectors = []

    for step in range(number_of_steps):
        if step == 0:
            u_vectors.append(np.array(vectors[step]))
            e_n = np.multiply(1 / matrix_len(u_vectors[step]), u_vectors[step])
            e_vectors.append(e_n)
            continue

        projections = []
        for n in range(step):
            projection_n = projection(u_vectors[n], vectors[step])
            projections.append(projection_n)

        u_n = vectors[step]
        for n_projection in projections:
            u_n = np.subtract(u_n, n_projection)

        u_vectors.append(u_n)
        e_n = np.multiply(1 / matrix_len(u_vectors[step]), u_vectors[step])
        e_vectors.append(e_n)

    q_matrix = np.array([vector for vector in e_vectors]).T
    r_matrix = np.dot(q_matrix.T, a)

    return [q_matrix,r_matrix]


matrix = np.array([
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
])
# matrix = np.array([
#     [1.4, 1.7, 2.9],
#     [0.7, 1, 3],
#     [1.9, 4.3, 2]
# ])
# matrix = np.array([
#     [1, 0],
#     [1, 1],
#     [0, 1]
# ])

qr_matrices = qr_decomposition(matrix)
print(f'Q MATRIX: \n{qr_matrices[0]}\n')
print(f'R MATRIX: \n{qr_matrices[1]}\n')

print(f'A MATRIX: \n{np.around(np.dot(qr_matrices[0], qr_matrices[1]), decimals=2)}')
