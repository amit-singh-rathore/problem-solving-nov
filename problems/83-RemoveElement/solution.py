def removeElement(nums, val):
    
    idx = 0 
    end = len(nums)-1
    while idx <= end:
        if nums[idx] == val:
            if nums[end] == val:
                end -=1
            else:
                nums[idx], nums[end] = nums[end], nums[idx]
        else:
            idx += 1
    return idx
        