# Explanation

We have four directions of movement and four boundaries.


Direction | move | Boundary | Change on completion 
--- | --- | --- | ---
L->R | 1 | left, right | +top
T->B | 2 | top, bottom | -right
R->L | 3 | right, left | -bottom
B->T | 4 | bottom, top | +left

to keep track of move we do a `move%4`
