def firstMissingPositive(nums):
    res = [0]*301
    for i in range(300):
        res[i]=i+1
    
    for item in nums:
        if item > 0 and  item < 302:
            res[item-1]=-1
    
    for i in range(300):
        if res[i] > 0:
            return res[i]
    return 1

numslist = [[1,2,0], [3,4,-1,1], [7,8,9,11,12]]
 
for nums in numslist:
    print(firstMissingPositive(nums))