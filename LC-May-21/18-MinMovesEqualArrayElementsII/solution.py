class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        target = nums[len(nums)//2]
        res = 0
        for n in nums:
            res += abs(target-n)
        return res