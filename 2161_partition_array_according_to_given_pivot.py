class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        left = []
        right = []
        same = []

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                same.append(num)

        return left + same + right


nums = [9,12,5,10,14,3,10]
pivot = 10
nums = [-3,4,3,2]
pivot = 2
print(Solution().pivotArray(nums, pivot))