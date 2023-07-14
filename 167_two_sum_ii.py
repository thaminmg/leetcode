class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        prevMap = {}
        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff] + 1, idx + 1]
            prevMap[num] = idx 
        return

nums = [2, 3, 4]
target = 6
print(Solution().twoSum(nums, target))