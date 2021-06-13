class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        h = num
        while l<= h:
            mid = (l + h) // 2
            n = mid*mid
            if n == num: return True
            if n > num: h = mid-1
            if n < num: l = mid + 1
        return False