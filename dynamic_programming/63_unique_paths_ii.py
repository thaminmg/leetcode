class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        dp[N - 1] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                print(r, c)
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c+ 1]
        return dp[0]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))