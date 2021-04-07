class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        res = nums[0]
        curr_max = nums[0]
        for item in nums[1:]:
            if curr_max < 0:
                curr_max = item
            else:
                curr_max = curr_max + item
            if curr_max > res:
                res = curr_max
        return res