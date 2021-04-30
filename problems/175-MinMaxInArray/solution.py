import random
randomlist = random.sample(range(0, 99999), 2000)

# Reverse case 2n-2 comparision
# Sorted case n-1
# Avg log2(n)
def minMax(nums):
    mxm = nums[0]
    mnm = nums[0]
    for i in range(1, len(nums)): 
        if (nums[i] > mxm):
            mxm = nums[i]
        elif (nums[i] < mnm):
            mnm = nums[i]
    
    return mnm, mxm
print(minMax(randomlist))

# always ~1.5 * n comparisions
def minMax(nums):
    def helper(nums, l, r):
        mnm , mxm = 0, 0
        if (l == r):
            mxm = nums[l]
            mnm = nums[l]
    
        elif (l + 1 == r):
            if (nums[l] < nums[r]):
                mxm = nums[r]
                mnm = nums[l]
            else:
                mxm = nums[l]
                mnm = nums[r]
        else:
            mid = l + (r - l)//2
            left_res = helper(nums, l, mid)
            right_res = helper(nums, mid+1, r)
            if (left_res[0] > right_res[0]):
                mnm = right_res[0]
            else:
                mnm = left_res[0]
            if (left_res[1] < right_res[1]):
                mxm = right_res[1]
            else:
                mxm = left_res[1]
        return mnm, mxm
        
    return helper(nums, 0, len(nums)-1)

# avg n/2
# Sorted either way n-2/1
def minMax(nums):
    mnm, mxm, i = 0, 0, 0
    if len(nums)%2!=0:
        mnm = nums[0]
        mxm = nums[0]
        i = 1
    else:
        if (nums[0] < nums[1]):
            mxm = nums[1]
            mnm = nums[0]
        else:
            mxm = nums[0]
            mnm = nums[1]
        i = 2
    while (i < len(nums)):
        if (nums[i] < nums[i+1]):
            if (nums[i] < mnm):
                mnm = nums[i]
            if (nums[i+1] > mxm):
                mxm = nums[i+1]
        else:
            if (nums[i] > mxm):
                mxm = nums[i]
            if (nums[i+1] < mnm):
                mnm = nums[i+1] 
        i = i + 2
    return  mnm, mxm

print(minMax(randomlist))
    