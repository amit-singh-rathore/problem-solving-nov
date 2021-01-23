def max_profit(prices):
    max_profit = 0
    min_price = prices[0]

    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        max_profit = max(max_profit, prices[i]-min_price)

    return max_profit
print(max_profit([7,1,5,3,6,4]))

