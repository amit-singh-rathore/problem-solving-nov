class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        l = len(heights)
        pq = []
        for i in range(l-1):
            jump = heights[i + 1] - heights[i]
            if jump <= 0: 
                continue
            heappush(pq, jump)
            if len(pq) > ladders:
                bricks -= heappop(pq)
            if(bricks < 0) : 
                return i
        return l - 1