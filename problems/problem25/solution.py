def findCheapestPrice(n, flights, src, dst, K):
    cost_dest = [float('inf') for i in range(n)]
    cost_dest[src] = 0
    for i in range(K + 1):
        cost_dest_ = cost_dest[:]
        for start, end, cost in flights:
            cost_dest_[end] = min(cost_dest_[end], cost_dest[start] + cost)
        cost_dest = cost_dest_
    
    if cost_dest[dst] == float('inf'):
        return -1
    
    return cost_dest[dst]

print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))