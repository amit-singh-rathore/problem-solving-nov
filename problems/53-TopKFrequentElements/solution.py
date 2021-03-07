from collections import Counter
from heapq import heappush, heappop

def topKFrequent(nums, k):
    freq_counter = Counter(nums)
    priority_queue = []
    for i in freq_counter:
        heappush(priority_queue, (-freq_counter[i], i))

    res = []
    while k:
        i, j = heappop(priority_queue)
        res.append(j)
        k -= 1

    return res
    
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    from collections import Counter
    
    freq_counter = Counter(nums)
    freq_sorted = sorted(freq_counter, key=freq_counter.get, reverse=True)
    return freq_sorted[:k]