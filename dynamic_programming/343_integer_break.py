class Solution:
    
    def integerBreak(self, n: int) -> int:
        # DP
        dp = {1: 1}

        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp[i] * dp[num - i]
                dp[num] = max(dp[num], val)
        return dp[n]

    # math solution using number of threes
    #     if n < 4: return n - 1

    #     noThree = n // 3
    #     res = 3 ** noThree
    #     if n % 3 == 1:
    #         res //= 3
    #         res *= 4
    #     elif n % 3 == 2:
    #         res *= 2
    #     return res
        