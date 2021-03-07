# Explanation

## Runtime Complexity
Linear -  O(nk)

## Memory Complexity
Constant - O(n)

## Logic
We solve this using dynamic programming.

We find 
```
min(array[idx], array[idx]+array[idx-1], array[idx]+array[idx-2], .... array[idx]+array[idx-k]
```