def min_cost_with_hops(array, k):
    idx_min_cost = [float('inf')] * len(array)
    idx_min_cost[0] = array[0]

    for i in range(1, len(array)):
        for j in range(1, k + 1):
            if i - j < 0:
                continue
            idx_min_cost[i] = min(idx_min_cost[i], array[i] + idx_min_cost[i - j])

    return idx_min_cost[-1]
        

print(min_cost_with_hops([20, 30, 40, 25, 15, 20, 28], 3))