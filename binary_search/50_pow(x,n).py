class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binaryExponent(x: float, n: int):
            if n == 0: return 1
            if n < 0: return 1 / binaryExponent(x, -1 * n)

            if n % 2 == 1:
                return x * binaryExponent(x * x, (n - 1) // 2)
            else:
                return binaryExponent(x * x, n // 2)
        return binaryExponent(x, n)