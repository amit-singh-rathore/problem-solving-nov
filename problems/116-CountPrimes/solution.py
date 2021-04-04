class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        primes = [True]*n
        primes[0] = False
        primes[1] = False
        
        loop_max_limit = math.ceil(math.sqrt(n))
        for i in range(2, loop_max_limit):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        return sum(primes)
        