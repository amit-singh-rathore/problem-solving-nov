class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first_index = -1
        second_index = -1
        
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                first_index = i
        
        if first_index == -1:
            nums.reverse()
            return
        
        for i in range(first_index+1, len(nums)):
            if nums[first_index] < nums[i]:
                second_index = i
        
        nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
        nums[first_index+1:] = nums[first_index+1:][::-1]