# Explanation

First we put the elements of the first column into a heap and track the row they came from. 
At each step, we remove the minimum element from the heap and push the next element from the row it came from 
At the jth step, you remove the jth smallest element, so after k steps you are done for a total cost of O(k log n) operations.

