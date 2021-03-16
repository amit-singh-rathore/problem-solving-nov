# Explanation

We move the pointers based on this rule: if we `height[left] <= height[right]`, then we increase the left pointer, otherwise we decrease the right pointer.
By moving closer we are reduicng the width of container. 

In doing so, we arrive at two possible scenarios: 

1. The next bar is still higher than or equal to the shorter bar of the two 
	- In this case the area we get will be less because the area is dictated by the shorter of the two bars and the shorter bar of the two remains the same; 
2. The next bar is shorter than the original shorter bar of the two 
	- In this case since the shorter bar of the two also getting smaller, area will decrease.

