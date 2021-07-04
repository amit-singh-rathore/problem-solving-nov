class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        first, second, third= nums[0], float('-inf'), float('-inf')
        
        if len(nums)<3: return max(nums)
        
        for num in nums:
            if (num > first):
                third, second, first = second, first, num
            elif second < num < first:
                third, second = second, num
            elif third < num < second:
                third = num
                        
        return third if third != float('-inf') else first