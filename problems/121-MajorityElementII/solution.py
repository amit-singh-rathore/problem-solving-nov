class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        
        for item in nums:
            counter[item] = counter.get(item, 0) + 1
        # for num in nums:
        #     if counter[num] > len(nums)//2:
        #         res.append(num)
        res = [key for key, val in counter.items() if val > len(nums)//3]
        return res
        
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c,n = Counter(nums), len(nums)
        return [_ for _ in c if c[_]>n//3]
        


