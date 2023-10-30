class Solution:
    def myPow(self, x: float, n: int) -> float:
        def my_pow(x, n):
            if n == 0: return 1
            if x == 0: return 0

            res = my_pow(x, n // 2)
            res = res * res

            return x * res if n % 2 == 1 else res
        return my_pow(x, n) if n >= 0 else 1 /my_pow(x, abs(n))