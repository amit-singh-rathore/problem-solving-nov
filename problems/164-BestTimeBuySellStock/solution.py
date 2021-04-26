class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cur_cp = prices[0]
        for i in range(1, len(prices)):
            if cur_cp < prices[i]:
                res = max(res, prices[i] - cur_cp)
            else:
                cur_cp = prices[i]
        return res