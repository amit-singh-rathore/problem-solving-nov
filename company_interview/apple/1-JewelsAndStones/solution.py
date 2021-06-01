class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        s = collections.Counter(stones)
        for key, val in s.items():
            if key in jewels:
                res += s[key]
        return res