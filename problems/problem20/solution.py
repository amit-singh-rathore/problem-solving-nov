def max_area(array):
    max_area = 0
    if len(array)<2:
        return max_area
    left = 0
    right = len(array)-1
    while left < right:
        max_area = max(max_area, min(array[left], array[right])*(right-left))
        if array[left] < array[right]:
            left +=1
        else:
            right -= 1
    return max_area
    

print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))