class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        stack = []
        
        for idx, val in enumerate(nums): 
            while stack and val > nums[stack[-1]]:
                result[stack.pop()] = val   
            stack.append(idx)
            
        for idx, val in enumerate(nums):  
            while stack and val > nums[stack[-1]]:
                result[stack.pop()] = val
                
        return result