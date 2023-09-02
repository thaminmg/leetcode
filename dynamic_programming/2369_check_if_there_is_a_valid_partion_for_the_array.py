class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        two = nums[-1] == nums[-2]
        if len(nums) == 2:
            return two
        three = (nums[-1] == nums[-2] == nums[-3]) or (nums[-3] + 1 == nums[-2] == nums[-1] - 1)
        dp = [three, two, False]
        for i in range(len(nums) - 4, -1, -1):
            cur = nums[i] == nums[i + 1] and dp[1]
            cur = cur or (nums[i] == nums[i + 1] == nums[i + 2] or  nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1) and dp[2]
            dp = [cur, dp[0], dp[1]]
        return dp[0]




nums = [993335,993336,993337,993338,993339,993340,993341]
# nums = [4,4,4,5,6]
nums = [473928,473929,473930]
print(Solution().validPartition(nums))