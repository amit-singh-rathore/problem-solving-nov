class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        for j in range(len(nums)):
            window_sum += nums[j]
            if window_sum < nums[j] * (j - i + 1):
                window_sum -= nums[i]
                i += 1
        return j - i + 1