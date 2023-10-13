class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # dp = [0] * n

        # for i in range(n):
        #     if i < 2:
        #         dp[i] = cost[i]
        #     else:
        #         dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        # return min(dp[-1], dp[-2]) 
        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]
             
      