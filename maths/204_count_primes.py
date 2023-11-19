class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [True] * n
        if n <= 1: return 0
        sieve[0], sieve[1] = False, False

        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i+i, n, i):
                    sieve[j] = False
        return sum(sieve)
        # def isPrime(n):
        #     if n < 0: return False
        #     x = 2
        #     while (x * x <= n):
        #         if n % x == 0:
        #             return False
        #         x += 1
        #     return True 

        # count = 0
        # for i in range(2, n):
        #     if isPrime(i):
        #         count += 1
        # return count
        