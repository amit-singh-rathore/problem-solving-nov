# DP Bottom UP
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n ==1 : 
            return 5
        dp= [[0] * (n+1) for i in range(5)]
        dp[0][1], dp[1][1], dp[2][1], dp[3][1], dp[4][1] = 1, 1, 1, 1, 1
        MOD = 1_000_000_007
        for i in range(2, n+1):
            dp[0][i] =  dp[1][i-1]
            dp[1][i] = (dp[0][i-1] + dp[2][i-1]) % MOD
            dp[2][i] = (dp[0][i-1] + dp[1][i-1] + dp[3][i-1] + dp[4][i-1]) % MOD
            dp[3][i] = (dp[2][i-1] + dp[4][i-1]) % MOD
            dp[4][i] =  dp[0][i-1]
        
        ans = 0
        for i in range(5): 
            ans = (ans + dp[i][n]) % MOD;
        return ans
  
# Space Optimized DP 
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n ==1 : 
            return 5
        a, e, i, o, u = 1, 1, 1, 1, 1
        
        MOD = 1_000_000_007
        for _ in range(2, n+1):
            a, e, i, o, u = (e + i + u) % MOD, (a + i) % MOD, (e + o) % MOD, i, (i + o) % MOD
        return (a + e + i + o + u) % MOD