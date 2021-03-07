def min_sum_zero(array):
  import math 
  array.sort()
  left = 0
  right = len(array)-1
  off_zero = math.inf
  while left < right:
    sum = array[left] + array[right]
    if abs(0-sum) < off_zero:
      res = (array[left], array[right])
      off_zero = abs(0-sum)
    if sum > 0:
      right -= 1
    else:
      left += 1
  return res

print(min_sum_zero([1, 60, -10, 70, -80, 85]))