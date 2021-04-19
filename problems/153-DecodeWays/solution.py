class Solution:
    def numDecodings(self, s: str) -> int:
        valid = set([str(x) for x in range(1, 27)])
        n = len(s)
        if n == 1:
            return int(s[0] in valid)

        Tabulation = [0] * n
        Tabulation[0] = int(s[0] in valid)
        Tabulation[1] = (s[0] in valid and s[1] in valid) + (s[:2] in valid)
        for i in range(2, n):
            Tabulation[i] = (s[i] in valid) * Tabulation[i - 1] + (s[i-1:i+1] in valid) * Tabulation[i - 2]

        return Tabulation[-1]