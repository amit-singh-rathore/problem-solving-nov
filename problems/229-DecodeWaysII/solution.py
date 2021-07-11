class Solution:
    def numDecodings(self, s: str) -> int:
        mod, dp = 1_000_000_007, [1, 0, 0]
        for code in s:
            dp_new = [0,0,0]
            if code == '*':
                dp_new[0] = 9*dp[0] + 9*dp[1] + 6*dp[2]
                dp_new[1] = dp[0]
                dp_new[2] = dp[0]
            else:
                dp_new[0]  = (code > '0') * dp[0] + dp[1] + (code <= '6') * dp[2]
                dp_new[1]  = (code == '1') * dp[0]
                dp_new[2]  = (code == '2') * dp[0]
            
                
            dp = [i % mod for i in dp_new]
        return dp[0]

# Early stopping for invalid cases
class Solution:
    def numDecodings(self, s: str) -> int:
        mod, dp = 1_000_000_007, [1, 0, 0]
        for idx, code in enumerate(s):
            if code == '0' and s[idx-1] not in ["1", "2", "*"]: return 0
            dp_new = [0,0,0]
            if code == '*':
                dp_new[0] = 9*dp[0] + 9*dp[1] + 6*dp[2]
                dp_new[1] = dp[0]
                dp_new[2] = dp[0]
            else:
                dp_new[0]  = (code > '0') * dp[0] + dp[1] + (code <= '6') * dp[2]
                dp_new[1]  = (code == '1') * dp[0]
                dp_new[2]  = (code == '2') * dp[0]
            
                
            dp = [i % mod for i in dp_new]
        return dp[0]