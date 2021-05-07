import math, collections
def numSquares(n):
    pf_sq = set([x**2 for x in range(1, math.ceil(n ** 0.5) + 1)])
    if n in pf_sq:
        return 1
    seen = {n}
    queue = collections.deque([(n, 0)])
    
    while queue:
        target, count = queue.popleft()
        if target == 0: 
            return count
        if target in pf_sq: 
            return count + 1
        for square in pf_sq:
            new_target = target - square
            if new_target == 0: 
                return count + 1
            if new_target in pf_sq: 
                return count + 2
            if new_target not in seen and new_target > 0:
                queue.append((new_target, count + 1))
                seen.add(new_target)
print(numSquares(11))