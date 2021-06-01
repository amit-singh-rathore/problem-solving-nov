class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while (n != 1):            
            dgt_sum = sum([i*i for i in list(map(int,str(n)))])
            if dgt_sum in seen:
                return False
            else:
                seen.add(dgt_sum)
            n = dgt_sum
        return True