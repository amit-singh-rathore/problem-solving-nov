
def divide(dividend, divisor):
    
    negative = False
    if (dividend > 0 > divisor) or (divisor > 0 > dividend):
        negative = True
    
    divisor = abs(divisor)
    dividend = abs(dividend)
    if divisor == 1:
        return -dividend if negative else dividend
    
    q = 1
    q_list = [q]
    decrement = [divisor]        
    while dividend >= divisor:
        q += q
        divisor += divisor
        q_list.append(q)
        decrement.append(divisor)

    quotient = 0
    for i in range(len(decrement)-1, -1, -1):
        if dividend >= decrement[i]:
            quotient += q_list[i]
            dividend -= decrement[i]
    
    return -quotient if negative else quotient
    
    
for tup in [(10,3), (7, -3), (12345678, 1), (-1234567, 1), (-20, -4)]:
    print(divide(tup[0], tup[1]))
    