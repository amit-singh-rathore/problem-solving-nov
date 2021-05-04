# Explanation

## False condition 

If we have more than one pair of adjacent elements, such that first is more then the next one

## True condition

If this element is the first or the last.

`nums[flip_idx-1] <= nums[flip_idx+1]` or `nums[flip_idx] <= nums[flip_idx+2]`.
