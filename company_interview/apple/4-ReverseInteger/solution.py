class Solution:
    def reverse(self, x: int) -> int:

        lb = -int(math.pow(2, 31))
        ub =  int(math.pow(2, 31)) - 1
        
        sign = 1 if x>0 else -1
        res = 0
        x = abs(x)
        while x > 0:
            x, r = divmod(x, 10)
            res = res*10 + r
        if res < lb or res > ub:
            return 0
        return res * sign