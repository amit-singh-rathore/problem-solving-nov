class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cnt = 0
        def dfs(path,diag):
            row = len(path)
            if row == n:
                self.cnt += 1
            else:
                for col in range(n):
                    if col not in path and col + row not in diag and col - row - n not in diag:
                        dfs(path + [col],diag + [col + row,col-row-n])
        dfs([],[])
        return self.cnt