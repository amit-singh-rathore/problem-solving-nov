class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ub = len(nums)
        res = float("inf")
        for i in range(ub-k+1):
            res = min(res, nums[i+k-1] - nums[i])
        return res