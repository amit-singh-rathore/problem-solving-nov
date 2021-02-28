def findMin(nums):
    left = 0 
    right = len(nums) - 1
    while left < right - 1:
        middle = (left + right) // 2

        if nums[middle] > nums[right]:
            left = middle
        else:
            right = middle if nums[middle] != nums[right] else right - 1
    if nums[left] < nums[right]:
        min_num = nums[left]
    else:
        min_num = nums[right]
        
    
    return min_num

print(findMin([4,5,6,6,7,1,1, 1,2]))