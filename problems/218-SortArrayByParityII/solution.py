class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:        
        n = len(nums)
        j = n-1
        
        for i in range(0, n, 2):
            if nums[i]%2==1:
                while( j >= 0 and nums[j]%2 == 1):
                    j -= 2
                if j >= 0:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums
                

