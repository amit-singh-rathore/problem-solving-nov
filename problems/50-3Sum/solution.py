def threeSum(nums):
    from collections import Counter
    
    counter = Counter(nums)
            
    def is_valid(num1, num2, num3):
        if num1 == num3 and num2 == num3:
            return counter[num1] >= 3
        if num1 == num2:
            return counter[num1] >= 2
        if num2 == num3:
            return counter[num2] >= 2
        return True
            
    unique_sorted = sorted(counter.keys())
    
    l = len(unique_sorted)
    res = []
    for i in range(l):
        num1 = unique_sorted[i]
        if num1 > 0: #one number has to -ve or 0
            break
        for j in range(i, l):
            num2 = unique_sorted[j] 
            num3 = 0 - num1 - num2
            if num2 > num3:
                break  
            if num3 in counter and is_valid(num1, num2, num3):
                res.append([num1, num2, num3])
    return res

print(threeSum([-1,0,0,0,1,2,-1,-4]))