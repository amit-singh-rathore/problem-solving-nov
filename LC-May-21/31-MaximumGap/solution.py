class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: 
            return 0
        lower, upper = min(nums), max(nums)
        step = max(1, (upper - lower)//(len(nums)-1))
        size = (upper - lower)//step + 1
        buckets = [[inf, -inf] for _ in range(size)]
        
        for num in nums: 
            i = (num - lower)//step
            l, u = buckets[i]
            buckets[i] = min(l, num), max(u, num)
        
        ans = 0
        prev = lower
        for i in range(size):
            l, u = buckets[i]
            if l < inf:
                ans = max(ans, l - prev)
                prev = u 
        return ans 