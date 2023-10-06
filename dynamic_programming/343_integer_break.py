class Solution:
    # math solution using number of threes
    def integerBreak(self, n: int) -> int:
        if n < 4: return n - 1

        noThree = n // 3
        res = 3 ** noThree
        if n % 3 == 1:
            res //= 3
            res *= 4
        elif n % 3 == 2:
            res *= 2
        return res
        