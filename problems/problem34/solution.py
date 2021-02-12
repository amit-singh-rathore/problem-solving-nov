def uniquePaths(m, n, dp = {}) -> int:
    if m == 1 & n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    if (m, n) in dp:
        return dp[(m,n)]

    dp[tuple([m, n])]= uniquePaths(m-1, n, dp) + uniquePaths(m, n-1, dp)
    return dp[(m, n)]

print(uniquePaths(3,7))


# def uniquePaths(m, n):
#     row = [0] * n
#     dp = [row for _ in range(m)]

#     for row in range(m):
#         for col in range(n):
#             if row==0 or col==0:
#                 dp[row][col] = 1
#             else:
#                 dp[row][col] =  dp[row-1][col] + dp[row][col-1]
#     return dp[m-1][n-1]
            
        