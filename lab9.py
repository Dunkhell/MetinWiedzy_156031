def gauss(matrix):
    column_len = len(matrix.T[0])

    for x in range(column_len):
        if matrix[x][x] == 0:
            raise ZeroDivisionError()

        for y in range(column_len):
            if x != y:
                factor = matrix[y][x] / matrix[x][x]

                for z in range(column_len + 1):
                    matrix[y][z] = matrix[y][z] - factor * matrix[x][z]
    return [matrix[i][column_len] / matrix[i][i] for i in range(column_len)]

# TODO: Macierz wektorów własnych
