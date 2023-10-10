def longestIncreasingSequence(nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[i] + dp[j])
        return max(dp)
        
sequence = [3, 2, 5, 1, 6, 3, 9, 2]
print(longestIncreasingSequence(sequence))
