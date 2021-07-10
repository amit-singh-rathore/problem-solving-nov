class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]: 
            return "0"
        if num1=="1": return num2
        if num2=="1": return num1 
        
        l1, l2 = len(num1), len(num2)
        
        res = [0] * (l1 + l2)

        for d1 in range(l1-1, -1, -1):
            for d2 in range(l2-1, -1, -1):
                mul = int(num1[d1]) * int(num2[d2])
                q, r = divmod(mul + res[d1 + d2 + 1], 10)
                res[d1 + d2 + 1] = r
                res[d1 + d2] += q 

        mul = "".join(map(str, res))
        return mul[1:] if mul[0] == "0" else mul
        