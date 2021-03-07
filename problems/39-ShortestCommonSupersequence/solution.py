
def shortestCommonSupersequence(str1, str2):
    dp = [[0 for j in range(len(str2)+1)]for i in range(len(str1)+1)]
    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            if str1[row-1] == str2[col-1]:
                dp[row][col] = dp[row-1][col-1] + 1
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
                
    res = ""
    i = len(dp)-1
    j = len(dp[0])-1
    while(i > 0 and j > 0):
        if str1[i-1] == str2[j-1]:
            res += str1[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                res += str1[i-1]
                i -= 1
            else:
                res += str2[j-1]
                j -= 1
    while(i > 0):
        res += str1[i-1]
        i -= 1
    while(j > 0):
        res += str2[j-1]
        j -= 1
    return res[::-1]

print(shortestCommonSupersequence('abac', 'cab'))