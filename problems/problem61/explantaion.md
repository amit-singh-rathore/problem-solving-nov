# Explanation

We solve this by BFS traversal of tree.

First, we put root into our queue(python deque).
On each iteration we extract all nodes from queue from the left and put all children to the rigtht.
We calculate average of elements in list and add it to final result.

