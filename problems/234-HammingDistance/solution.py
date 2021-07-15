class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x ^= y
        
        res = 0
        
        while(x>0):
            x &= x-1
            res += 1
        return res