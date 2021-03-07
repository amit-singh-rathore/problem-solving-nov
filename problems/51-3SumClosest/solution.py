import math

def threeSumClosest(nums, target):
    res = off_margin = math.inf
    nums.sort()
    
    i = j = 0
        
    for idx in range(len(nums)-1):
        i = idx + 1
        j = len(nums) - 1
            
        while i < j:
            val = nums[i] + nums[j] + nums[idx]
            cur_off_margin = target - val
            if cur_off_margin == 0:
                return val
            elif cur_off_margin < 0:
                j -= 1
            else:
                i += 1
            cur_off_margin = abs(cur_off_margin)
            if off_margin > cur_off_margin:
                off_margin = cur_off_margin
                res = val
    return res
        
print(threeSumClosest([-1,2,1,1,-4], 1))
        
