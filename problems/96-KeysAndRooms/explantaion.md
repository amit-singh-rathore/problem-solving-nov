# Explanation

We start from room 0, collect the keys present in room 0. 
We add all the keys that we collect in a queue. 
We visit the next rooms by taking keys present in our queue. 
Each time we visit a new room, we add all the keys present in that room to the queue.

To avoid circular dependency we use array of room index visited.
