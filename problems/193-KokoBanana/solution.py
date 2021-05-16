class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r
        while l<=r:
            mid = (l+r)//2
            hours = 0
            if sum((pile-1) // mid + 1 for pile in piles) <= h:
                ans = min(ans, mid)
                r = mid-1
            else:
                l = mid+1
            
        return ans