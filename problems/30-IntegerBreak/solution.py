def integerBreak(n):
    dp = [i-1 for i in range(n+1)]
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], max(j, dp[j]) * max(i-j, dp[i-j]))
    return dp[-1]
    
print(integerBreak(10))