# Explanation

## Dynamic programming

DP takes a bottom-up approach to a problem. We start with the simplest of problems (base case). 

In this problem base problem is --> What is the maximum value of Gold we can acquire if we just had to reach cell (0,0)? The answer is cell value itself.

What about (0, 1) --> value of Gold acquired at (0, 0) + cell value at (0, 1)

Similarly for (1, 0) --> value of Gold acquired at (0, 0) + cell value at (1, 0)

Now for cell (1, 1) --> Max of (cell above (0, 1), cell to left(1,0)) + cell value.