import math

def maxSubarraySum(arr, w):
    if w > len(arr) or w==0:
        return None
    maxSum = sum(arr[0:w])
    tempSum = sum(arr[0:w])
    for i in range(w, len(arr)):
        tempSum = tempSum - arr[i - w] + arr[i]
        if (tempSum > maxSum):
            maxSum = tempSum
    return maxSum
    
    
print(maxSubarraySum([1,2,4,-5, 6, 1, 3, -5, 2, 6, 9, -1], 13))