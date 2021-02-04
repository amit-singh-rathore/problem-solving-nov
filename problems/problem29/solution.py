from heapq import *

def kthSmallest(matrix, k):
    N = len(matrix[0])
    min_heap = []
    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], 0, i))
    counter, number = 0, 0
    while min_heap:
        number, idx, row_num = heappop(min_heap)
        counter += 1
        if counter == k:
            break
        if N > idx+1:
            heappush(min_heap, (matrix[row_num][idx+1], idx+1, row_num))
    return number
    
# matrix = [[2, 6, 8], [3,7, 10], [5, 8, 11]]
# k = 5

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(kthSmallest(matrix, k))