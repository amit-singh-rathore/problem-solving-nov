def maxGoldSum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    gold_sum_matrix = matrix[:]

    for i in range(1,cols):
        gold_sum_matrix[0][i] += gold_sum_matrix[0][i-1]

    for i in range(1,rows):
        gold_sum_matrix[i][0] += gold_sum_matrix[i-1][0]

    for i in range(1,rows):
        for j in range(1,cols):
            gold_sum_matrix[i][j] += max(gold_sum_matrix[i-1][j],gold_sum_matrix[i][j-1])

    return gold_sum_matrix[-1][-1]
    
    
print(maxGoldSum([[1,2,4],[-5, 6, 1], [3, -5, 2], [6, 9, -1]]))