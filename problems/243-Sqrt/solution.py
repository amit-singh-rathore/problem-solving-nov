class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        start, end = 2, x//2
        
        while start <= end:
            mid = start + (end-start)//2
            
            num = mid * mid
            
            if num > x:
                end = mid - 1
            elif num < x:
                start = mid + 1
            else:
                return mid
        return end