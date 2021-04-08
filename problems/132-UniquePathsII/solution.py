class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: 
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0] * n for _ in obstacleGrid]
        grid[0][0] = 1
        
        for i in range(1,m):
            if obstacleGrid[i][0] != 1:
                    grid[i][0] += grid[i-1][0]

        for j in range(1,n):
            if obstacleGrid[0][j] != 1:
                    grid[0][j] += grid[0][j-1]
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                
        return grid[-1][-1]