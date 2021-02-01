# Explanation

1. A basic solution will be running a loop through the array for each and every element to check if it appears more than n/2 times.  -- O(n^2)

2. A better solution will come if we sort the array. In that case all occurrences will appear side by side, so that now we can check if any one of them are placed consecutively more than n/2 times. O(nlogn) 

3. We can use of disctionary to store the count of occurence of each element. This will work with O(n) time complexity with extra space.

4. Boyer–Moore majority vote algorithm. It has O(n) time complexity and O(1) space complexity.


