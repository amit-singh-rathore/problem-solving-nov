# Explanation

## Will solve the problem in single scan

1. We keep an count of max 1s sequence by flipping first **m** 0s. 
2. Once we encounter a zero after exhausting the flips, we remove the first 0 from left and get the new length 
3. Keep in sliding this to see the max length 
4. for the window with max length flipped indexes are returnrd