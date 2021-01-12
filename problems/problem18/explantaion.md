# Explanation

## We will solve this in two scan of the array.

1. Sort the array
2. Move from right to left, if weight or sum of weigts at left and right index are > than limit increase boat count by one. Decrease the right pointer.
3. If weight of right and left indices are smaller or equal to lmit increase the boat count. Increase the left index and decrease the right index.


