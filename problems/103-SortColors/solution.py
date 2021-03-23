class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums)-1
        index = 0
        while index <= end:
            if nums[index] == 0:
                nums[start], nums[index] = nums[index], nums[start]
                start += 1
                index += 1
            elif nums[index] == 2:
                nums[end], nums[index] = nums[index], nums[end]
                end -= 1
            elif nums[index] == 1:
                index += 1
        return nums