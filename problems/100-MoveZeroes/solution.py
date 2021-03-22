class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <=1:
            return
        curr_idx  = 0
        non_zero_idx = 0
        
        
        while curr_idx <= len(nums)-1:
            if nums[curr_idx] != 0:
                nums[non_zero_idx] = nums[curr_idx]
                non_zero_idx += 1
            curr_idx += 1
        
        while non_zero_idx <= len(nums)-1:
            nums[non_zero_idx] = 0
            non_zero_idx += 1
            