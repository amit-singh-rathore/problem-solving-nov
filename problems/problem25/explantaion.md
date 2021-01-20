# Explanation


## Logic
Solve this using DP. 
The optimal solution at the node at higher level is composed by
 - optimal solution at lower level node + the cost of the flight from current node to lower level node
 - Inifinite if we cannt get to dst from current node

