class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.low, self.high = [], []
        
    def addNum(self, num: int) -> None:
        heappush(self.high, -heappushpop(self.low, -num))
        if len(self.low) < len(self.high):
            heappush(self.low, -heappop(self.high))
            
    def findMedian(self) -> float:
        return -self.low[0] if len(self.low) > len(self.high) else (-self.low[0]+self.high[0])/2


# Optimization

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_heap = []
        self.right_heap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.size += 1
        if self.size == 1:
            heapq.heappush(self.right_heap, num)
            return
        right_min = self.right_heap[0]
        
        if len(self.right_heap) > len(self.left_heap):
            if num < right_min:
                heapq.heappush(self.left_heap, -num)
            else:
                heapq.heappush(self.left_heap, -heapq.heappushpop(self.right_heap, num))
        else:
            if num > right_min:
                heapq.heappush(self.right_heap, num)
            else:
                heapq.heappush(self.right_heap, -heapq.heappushpop(self.left_heap, -num))
        
        
    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (-self.left_heap[0]+self.right_heap[0])/2
        else:
            return self.right_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()