class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        updated = set()
        for row in range(m):
            for col in range(n):
                loc=(row,col)
                if loc in updated:
                    continue
                if matrix[row][col] == 0 and loc not in updated:
                    for r in range(m):
                        if matrix[r][col] != 0:
                            matrix[r][col] = 0
                            updated.add((r,col))
                    for c in range(n):
                        if matrix[row][c] != 0:
                            matrix[row][c] = 0
                            updated.add((row,c)) 
        
        