# Memory optimized
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_run = 0
        cur_run = 0
        prev=False
        for i in range(len(nums)):
            if nums[i] == 1:
                if not prev:
                    prev = True
                cur_run += 1
            elif prev :
                prev = False
                max_run = max(max_run, cur_run)
                cur_run = 0
        max_run = max(max_run, cur_run)
        return max_run
  
# Time optimized
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        runs=[]
        cur_run=0
        for num in nums:
            if num == 1:
                cur_run += 1
            else:
                runs.append(cur_run)
                cur_run = 0
        
        runs.append(cur_run)
        
        return max(runs)