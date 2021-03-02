from heapq import heappush, heappop

def kSmallestPairs(nums1, nums2, k):
    if len(nums1) == 0 or len(nums2) == 0:
        return []

    min_heap = [(nums1[0] + nums2[0], 0, 0)]
    visited = set((0, 0))
    i = 0
    result = []
    while i < k and len(min_heap) > 0:
        _, idx1, idx2 = heappop(min_heap)
        result.append([nums1[idx1], nums2[idx2]])
        if idx2 + 1 < len(nums2) and (idx1, idx2 + 1) not in visited:
            heappush(min_heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
            visited.add((idx1, idx2 + 1))
        
        if idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in visited:
            heappush(min_heap, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
            visited.add((idx1 + 1, idx2))
            
        i += 1
        
    return result
    
print(kSmallestPairs([1,1,2], [1,2,3], 2))