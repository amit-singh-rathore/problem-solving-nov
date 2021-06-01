class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for row in range(1, len(costs)):
            costs[row][0] += min(costs[row - 1][1], costs[row - 1][2])
            costs[row][1] += min(costs[row - 1][0], costs[row - 1][2])
            costs[row][2] += min(costs[row - 1][0], costs[row - 1][1])

        if len(costs) == 0: 
            return 0
        return min(costs[len(costs) - 1])