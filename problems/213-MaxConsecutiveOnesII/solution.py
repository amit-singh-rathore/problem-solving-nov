class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_run = 0
        cur_run = 0 
        max_run = 0
        
        for i in nums:
            if i == 0:
                max_run = max(cur_run + prev_run, max_run)
                prev_run = cur_run + 1
                cur_run = 0
            elif i == 1:
                cur_run += 1
  
        max_run = max(cur_run + prev_run, max_run)
    
        return max_run