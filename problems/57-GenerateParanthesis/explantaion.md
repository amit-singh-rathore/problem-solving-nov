# Explanation

1. Valid parethesis = ```()```
2. Using this we can generate combination of valid one if we try to place another ```()``` anywhere in the valid string. 
3. In case of two we have three places to the right (before), middle, right(after). So we get ```["()()", "(())"]```.
4. Now these two become valid again for the first we can try to place "()". This will give us ```["()()()", "(())()", "()(())", "(()())", "((()))"]```
5. And so on...

