def fib():
    penultimate = 0
    previous = 1
    
    def next_item():
        nonlocal penultimate, previous
        next_number = penultimate, previous
        penultimate, previous = previous, penultimate
        return next_number
        
    return next_item
    
fibonacci = fib()
N = 10
for i in range (2, N+1):
    number = fibonacci()
    print( number, end=' ')
