# Explanation

```
[1, 1, 2, 2, 3, 3]
 0, 1, 2, 3, 4, 5
 ```
 As we see above for a well formed pairs start at even index (0,2,4...). 
 If there is a number appering only once then pairs after that will start at odd place.
 Using binary search we find the half where the single appearing number is present.
 
 `nums[m] != nums[m - 1] and nums[m] != nums[m + 1]` will give the number.



