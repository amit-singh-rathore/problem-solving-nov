class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        unique = set(nums)
        max_len = 1
        
        for num in nums:
            if num - 1 not in unique:
                count = 1
                while num + 1 in unique:
                    count += 1
                    num += 1
                max_len = max(max_len, count)
        return max_len