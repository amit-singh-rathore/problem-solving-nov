def permute(self, nums: List[int]) -> List[List[int]]:
    
    if len(nums)==0:
        return []
    
    if len(nums)==1:
        return [nums]
    res = []
    
    for idx in range(len(nums)):
        
        curr = nums[idx]
        lst_wo_cur = nums[:idx]+nums[idx+1:]
        
        for permutation in self.permute(lst_wo_cur):
            res.append(permutation+[curr])
    
    return res