class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, running_sum, min_size = 0, 0, len(nums)+1
        for end in range(len(nums)):
            running_sum += nums[end]
            while running_sum >= target:
                running_sum -= nums[start]
                min_size = min(min_size, end-start+1)
                start += 1
        return min_size if min_size <= len(nums) else 0