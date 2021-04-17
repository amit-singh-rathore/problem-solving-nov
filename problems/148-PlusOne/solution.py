class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n  = len(digits)
        carry = 1
        for i in range(n-1, -1, -1):
            carry, digit = divmod(digits[i]+carry, 10)
            digits[i] = digit
            
        if carry>0:
            return [carry]+digits
        else:
            return digits