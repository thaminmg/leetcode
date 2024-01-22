class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            temp = abs(nums[i])
            if temp > n:
                continue
            temp -= 1
            if nums[temp] > 0:
                nums[temp] *= -1

        for i in range(n):
            if nums[i] >= 0:
                return (i + 1)
        return n + 1
            
            
        