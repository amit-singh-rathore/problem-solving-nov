class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        set_sum = 3 * (sum(set(nums)))
        return (set_sum - s)//2