class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 3: 
            return max(nums)
        
        tabulation = [0] * (size + 1) 
        
        tabulation[1], tabulation[2] = nums[0], nums[1]
        
        
        for i in range(2, size): 
            tabulation[i+1] = max(tabulation[i-1], tabulation[i-2]) + nums[i]
            
        return max(tabulation[-1], tabulation[-2])
        