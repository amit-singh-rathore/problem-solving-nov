# Explanation

Since we are interested in sum being zero and order does not matter we create a map of element and their occurences. 
This will remove repeated computaion for same number having multiple apparence.
We take a count as well to ensure we have enough of those. 
E.g. -4 , -4 , 8 can be a valid triplet only if -4 appears more than twice. Similary 0,0,0 is valid only if 0 appears thrice.

For 3 elements sum to be zero 1 number has to be negative or 0 ( case where all three nums are zero). 
So our outer loop runs only for number which are less than or equal to 0.
Second number can be either positive negative and zero, but has to be greater than equal to first number. 
So second loop runs from previous loops till the end.
Third number is nothing but (0 - num1 -num2)
We check if the third number is present or not.
