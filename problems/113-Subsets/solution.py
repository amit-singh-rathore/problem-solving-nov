class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        for i in range(len(nums)):
            si = len(res)
            for j in range(si):
                sl = res[j][:] #copy 
                sl.append(nums[i])
                res.append(sl)
        
        return res