def longestCommonSubsequence(text1, text2):
    dp = [[float('-inf') for j in range(len(text2)+1)]for i in range(len(text1)+1)]
    for row in range(len(dp)):
        for col in range(len(dp[0])):
            if row == 0 or col == 0:
                dp[row][col] = 0
            elif text1[row-1] == text2[col-1]:
                dp[row][col] = dp[row-1][col-1]+1
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
    return dp[-1][-1]