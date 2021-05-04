class Solution:
    def checkPossibility(self, nums):
        flip_idx, n = -1, len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                if flip_idx != -1: 
                    return False
                flip_idx = i
        if flip_idx in [-1, 0, n-2]:
            return True
        if nums[flip_idx-1] <= nums[flip_idx+1]:
            return True
        if nums[flip_idx] <= nums[flip_idx+2]:
            return True