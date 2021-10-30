import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.top_k = nums
        self.k = k
        heapq.heapify(self.top_k)
        
        while len(self.top_k)> self.k:
            heapq.heappop(self.top_k)

    def add(self, val: int) -> int:
        heapq.heappush(self.top_k, val)
        if len(self.top_k)> self.k:
            heapq.heappop(self.top_k)
        return self.top_k[0]
            
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)