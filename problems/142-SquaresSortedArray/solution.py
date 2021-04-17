class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        start, end = 0, n-1
        res = [0]*n
        idx = n-1
        
        while end > -1 and idx >-1:
            if abs(nums[start]) > abs(nums[end]):
                res[idx] = nums[start] * nums[start]
                start +=1
            else:
                res[idx] = nums[end] * nums[end]
                end -= 1
            idx -= 1
        
        return res