class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        if (row * col) != r*c:
            return mat
        res = [[0] * c for _ in range(r)]
        new_row = 0
        for i in range(row):
            for j in range(col):
                res[new_row//c][new_row%c] = mat[i][j]
                new_row += 1      
        return res


