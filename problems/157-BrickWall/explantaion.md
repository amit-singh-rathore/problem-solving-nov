# Explanation

We see the gaps in each row and note its position.
We create a dictionary with the position as key and number of gaps in that position.
Then we select the index with maxgap. Number bricks to cut will be len(wall) - num_gaps. 