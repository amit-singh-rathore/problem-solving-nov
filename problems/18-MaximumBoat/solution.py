def boat_count(array, limit):
    left = 0
    right = len(array)-1
    
    res = 0
    array.sort()
    
    while left <= right:
        if array[right]>=limit:
            res += 1
            right -= 1
        elif array[right]+array[left]>limit:
            res +=1
            right -= 1
        else:
            res +=1
            left += 1
            right -= 1
    
    return res

print(boat_count([2, 1, 4, 3], 4))