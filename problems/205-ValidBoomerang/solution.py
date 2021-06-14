class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1, p2, p3 = points
        
        x1 = p1[0] - p2[0]
        x2 = p2[0] - p3[0]
        y1 = p1[1] - p2[1]
        y2 = p2[1] - p3[1]
        
        if (x1*y2)==(x2*y1):
            return False
        return True