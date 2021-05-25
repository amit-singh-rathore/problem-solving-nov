class Solution:
    def Valid(self, queen, n, row, col):
        for i in range(n):
            if queen[i][col] == 'Q':
                return False
        for i in range(col,-1,-1):
            if queen[row][i] == 'Q':
                return False
        for (i,j) in zip(range(row,-1,-1),range(col,-1,-1)):
            if queen[i][j] == 'Q':
                return False
        for (i,j) in zip(range(row,n),range(col,-1,-1)):
            if queen[i][j] == 'Q':
                return False
        return True
    
    def SolveNQueens(self, queen, n, col):
        if col >= n:
            self.ans.append(["".join(queen[i]) for i in range(n)])
            return None
        for row in range(n):
            if self.Valid(queen, n, row, col):
                queen[row][col] = 'Q'
                self.SolveNQueens(queen, n, col + 1)
                queen[row][col] = '.'
        return None
            
    def solveNQueens(self, n: int) -> List[List[str]]:
        queen = [['.' for i in range(n)] for i in range(n)]
        
        self.ans = []
        self.SolveNQueens(queen, n, 0)
        return self.ans