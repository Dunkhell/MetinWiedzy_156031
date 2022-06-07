def gauss(matrix):
    column_len = len(matrix.T[0])

    for x in range(column_len):
        if matrix[x][x] == 0:
            matrix[x][x] = 1

        for y in range(column_len):
            if x != y:
                factor = matrix[y][x] / matrix[x][x]

                for z in range(column_len + 1):
                    matrix[y][z] = matrix[y][z] - factor * matrix[x][z]
    return [matrix[i][column_len] / matrix[i][i] for i in range(column_len)]


def macierz_wlasnosci(matrix, wartosc):
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[0]):
            if x == y:
                matrix[x][y] = matrix[x][y] - wartosc

    return matrix
