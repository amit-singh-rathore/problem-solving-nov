# Explanation

## Runtime Complexity
Linear -  O(n)

## Memory Complexity
Constant - O(1)

## Logic

We start from the right end of the array. We initialize two pointers.
1. zero_idx: Denotes the first index from right where the value is 0.
2. non_zero_idx: Denotes the index where we have a value other than zero which is smaller than zero_idx

Whenver we encounter a value which is not equal to zero at non_zero_idx and and we have a zero value at zero_idx we swap.
Then we decreament the value of non_zero_idx by 1. 

If we see a non zero value at zero_idx we decreament both non_zero_idx and zero_idx by 1.

We do this untill all zeros are moved to left.