def fib():
    penultimate = 0
    previous = 1
    
    def next_item():
        nonlocal penultimate, previous
        next_number = penultimate + previous
        penultimate, previous = previous, next_number
        return next_number
        
    return next_item
    
fibonacci = fib()
N = 10
for i in range (2, N+1):
    number = fibonacci()
    print( f"{number}", end=' ')


# Using list comprehension
n = 10
fib = [0, 1]
[fib.append(fib(-2)+fib(-1)) for _ in range(n)]
return fib