def transpose(matrix):
    matrix_t = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    
    '''
    print(matrix_t)
    matrix_TT = [[0] * len(matrix)] * len(matrix[0])
    print(matrix_TT)'''

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            matrix_t[i][j] = matrix[j][i]
    return matrix_t

print(transpose([[1, 3, 5], [2, 4, 6]]))