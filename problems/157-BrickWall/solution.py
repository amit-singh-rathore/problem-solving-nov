class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gap_map = {}
        wall_limit = sum(wall[0])
        max_gap = 0
        for row in wall:
            key = row[0]
            while key < wall_limit:
                for item in row[1:]:
                    if key in gap_map:
                        gap_map[key] += 1
                    else:
                        gap_map[key] = 1
                    max_gap = max(max_gap, gap_map[key])
                    key += item
        return len(wall)-max_gap