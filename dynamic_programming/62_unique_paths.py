class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        dp[m-1][n-1] = 1
        
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if r + 1 < m and c + 1 < n:
                    dp[r][c] = dp[r + 1][c] + dp [r][c + 1]
                elif r + 1 >= m and c + 1 < n:
                    dp[r][c] = dp [r][c + 1]
                elif c + 1 >= n and r + 1 < m:
                    dp[r][c] = dp[r + 1][c]
        return dp[0][0]

m = 3
n = 2
print(Solution().uniquePaths(m,n))