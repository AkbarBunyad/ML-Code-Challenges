def reshape(matrix, new_shape):
    if len(matrix) * len(matrix[0]) != new_shape[0] * new_shape[1]:
        return -1
    new_matrix = [[0 for _ in range(new_shape[1])] for _ in range(new_shape[0])]
    row, col = 0, 0
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            new_matrix[i][j] = matrix[row][col]
            col += 1
            if col == len(matrix[0]):
                col = 0
                row += 1
    return new_matrix

print(reshape([[1, 2, 3, 4], [5, 6, 7, 8]], [4, 2]))

# other way, using numpy
import numpy as np
def resh(matrix, new_shape):
    return np.reshape(matrix, new_shape).tolist()

print(resh([[1, 2, 3, 4], [5, 6, 7, 8]], [4, 2]))
