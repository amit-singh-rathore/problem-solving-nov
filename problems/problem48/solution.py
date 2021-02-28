def findMin(nums):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        
        prev=(mid-1+len(nums))%len(nums)
        next_=(mid+1)%len(nums) 
        if nums[left]<=nums[right]:
            return nums[left]
        else:
            if nums[prev]> nums[mid]< nums[next_]:
                return nums[mid] 
            elif nums[left]<=nums[mid]:
                left=mid+1
            else:
                left=mid-1