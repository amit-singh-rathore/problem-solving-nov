class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buying_state_value, selling_state_value = 0, -prices[0]
        for i in range(1, len(prices)):
            buying_state_value = max(buying_state_value, selling_state_value + prices[i] - fee)
            selling_state_value = max(selling_state_value, buying_state_value - prices[i])

        return buying_state_value