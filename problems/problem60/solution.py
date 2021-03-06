def get_area(grid, row, col):
	island_area = 1
	directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	if (row < 0 or row >= m or col < 0 or col >= n) or grid[row][col]==0:
		return 0

	grid[row][col] = 0
	for direction in directions:
		island_area += get_area(grid, row + direction[0], col + direction[1])
	return island_area

def maxAreaOfIsland(grid):
	
	m = len(grid)
	n = len(grid[0])
	
	max_area = 0

	for i in range(m):
		for j in range(n):
			if grid[i][j]:
				max_area = max(max_area, get_area(grid, i, j))

	return max_area