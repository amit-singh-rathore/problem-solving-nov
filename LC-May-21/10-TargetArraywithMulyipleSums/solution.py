class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        heap = [-item for item in target] # changing sign to make this max heap
        heapq.heapify(heap)
        
        cum_sum = sum(target)
        
        if len(target) ==1: 
            return target[0] == 1
        
        while cum_sum > len(target): 
            curr = -1 * heapq.heappop(heap) # Pop the last/greatest item
            new_cum_sum = cum_sum - curr 
            if new_cum_sum > curr : 
                return False
            if new_cum_sum ==1: 
                return True
            prev = curr % new_cum_sum 
            if prev < 1: 
                return False
            cum_sum = new_cum_sum + prev # new array becomes [9, 3, 5] --> [1, 3, 5]
            heapq.heappush(heap, -prev)
            
        return True