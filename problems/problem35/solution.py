def canJump(nums):
    max_idx = 0
    for idx, value in enumerate(nums):
        if idx > max_idx:
            return False
        max_idx = max(max_idx, idx+value)
    return True
        
print(canJump([3,2,1,0,4]))