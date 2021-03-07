def dailyTemperatures(T):
    stack = []
    res = [0]*(len(T))
    for idx in range(len(T)):
        while stack and T[idx] > T[stack[-1]]: 
            i = stack.pop()
            res[i] = idx - i
        stack.append(idx)
    return res
    
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))