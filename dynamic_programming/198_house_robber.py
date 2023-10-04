class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(n):
            dp[i + 1] = max(dp[i], nums[i] + dp[i - 1])
        return dp[-1]
        