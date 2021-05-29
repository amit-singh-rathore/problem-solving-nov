## Explanation

We need to find the maximum sum of subarrray (where elements in subarray is unique) in an array.
We do so by using Sliding Window technique. 3. Longest Substring Without Repeating Characters
To keep track of last index of a number we use dictionary.
Once we see the number again we postion our starting point as last seen index+1.