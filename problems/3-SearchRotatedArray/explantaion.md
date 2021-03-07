# Explanation

## Runtime Complexity
Logarithmic O(logn)

## Memory Complexity
Logarithmic, O(logn)

## Logic
The solution is based on the fact that of a sorted + rotated array is that when we divide it into two halves, at least one of the two halves will always be sorted. In sorted area halves we can search element by binary serach. 

We find which half is sorted by comparing start and end element of each half. 
Then we find if the key lies in that half or not. (extreme comparision)

Note: This solution works with array of unique elements.