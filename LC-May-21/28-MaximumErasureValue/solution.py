class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = dict()
        ans = sum = 0
        l = 0
        for idx, num in enumerate(nums):
            if num in seen:
                index = seen[num]
                while l <= index:  # Move the left side until index + 1
                    del seen[nums[l]]
                    sum -= nums[l]
                    l += 1

            seen[num] = idx
            sum += num
            ans = max(ans, sum)
        return ans