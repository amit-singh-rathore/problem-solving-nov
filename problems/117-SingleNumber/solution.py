class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # s = sum(nums)
        # set_sum = 2 * (sum(set(nums)))
        # return set_sum - s
        
        # unique = set()
        # for item in nums:
        #     if item in unique:
        #         unique.remove(item)
        #     else:
        #         unique.add(item)
        # return list(unique)[0]
        
        xor_till_last = nums[0]
        
        for item in nums[1:]:
            xor_till_last = xor_till_last^item
            print(xor_till_last)
        return xor_till_last
            
        
        #return reduce(lambda elem1, elem2: elem1^elem2, nums)
        
        