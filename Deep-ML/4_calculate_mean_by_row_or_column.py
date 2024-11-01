def calculate_mean(matrix, mode):
    if mode == 'column':
        res = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix[0])):
            sum = 0
            for j in range(len(matrix)):
                sum += matrix[j][i]
            res[i] = sum / len(matrix)
        return res
    elif mode == 'row':
        res = [0 for _ in range(len(matrix))]
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix[0])):
                sum += matrix[i][j]
            res[i] = sum / len(matrix[0])
        return res
    else:
        return -1

print(calculate_mean([[1, 2, 3, 4], [5, 6, 7, 8]], 'column'))
