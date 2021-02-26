def brokenCalc(X, Y):
    ans = 0
    while(Y > X):
        ans += 1
        if Y%2 == 0:
            Y = Y//2
            
        else:
            Y = Y+1
            
    return ans +(X-Y)

print(brokenCalc(4, 17))