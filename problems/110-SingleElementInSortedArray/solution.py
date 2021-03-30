class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r)//2 
            is_even = (r-m)%2==0

            if nums[m]==nums[m +1]:
                if is_even:
                    l = m+2
                else:
                    r = m -1       
            elif nums[m]==nums[m -1]:
                
                if is_even:
                    r= m-2

                else:
                    l =m+1

            else:
                return nums[m]

        return nums[l]