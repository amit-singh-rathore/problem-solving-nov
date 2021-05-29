from sortedcontainers import SortedList
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        from heapq import heapify, heappop, heappush
        
        heapify(sticks)
        res = 0
        
        for i in range(len(sticks) - 1):
            cost = heappop(sticks) + heappop(sticks)
            res += cost
            heappush(sticks, cost)
        return res