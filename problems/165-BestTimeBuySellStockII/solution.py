class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur_cp = 10001
        for i in range(len(prices)):
            if prices[i] > cur_cp:
                res += prices[i] - cur_cp
            cur_cp = prices[i]
        return res