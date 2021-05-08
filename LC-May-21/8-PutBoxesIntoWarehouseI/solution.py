class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        for i in range(1, len(warehouse)):
            warehouse[i]= min(warehouse[i], warehouse[i-1])
            
        boxes.sort(reverse=True)
        
        j = 0
        res = 0
        for height in warehouse:
            while j < len(boxes) and boxes[j] > height: 
                j += 1
            if j >= len(boxes):
                break
            res += 1
            j += 1
        return res