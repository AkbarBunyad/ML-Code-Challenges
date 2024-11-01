def computation(matrix, vect):
    if len(matrix[0]) != len(vect):
        return -1
    result = [0] * len(matrix)
    for i in range(len(vect)):
        for j in range(len(matrix)):
            result[j] += vect[i] * matrix[j][i]
    return result

print(computation([[1, 3, 5], [2, 4, 6]], [1, 2, 3]))