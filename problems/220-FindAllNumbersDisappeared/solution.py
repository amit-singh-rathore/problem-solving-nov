class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = [False] * (n)
        for item in nums:
            x[item-1] = item
        return [idx for idx, p in enumerate(x, 1) if not p]