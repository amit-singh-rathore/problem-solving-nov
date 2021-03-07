def remove_island(grid, i, j, m, n):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if (i < 0 or i >= m or j < 0 or j >= n):
        return None
    if grid[i][j] == '0':
        return None
    grid[i][j] = '0'
    
    for direction in directions:
        remove_island(grid, i + direction[0], j+ direction[1], m, n)

def numIslands(grid):
    m = len(grid)
    n = len(grid[0])
    num_islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                print(i, j)
                num_islands += 1
                remove_island(grid, i, j, m, n)
                print(grid)
    return num_islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))