def fizzbuzz(num):
    divisible_by_3 = (num % 3 == 0) 
    divisible_by_5 = (num % 5 == 0)
    if (divisible_by_3 or divisible_by_5):
        return (divisible_by_3 * 'Fizz') + (divisible_by_5 * 'Buzz')
    return str(num)

print(', '.join([fizzbuzz(x) for x in range(1,51)]))