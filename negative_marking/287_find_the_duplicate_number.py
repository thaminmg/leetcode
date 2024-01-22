class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Negative marking
        for i in range(len(nums)):
            pos = abs(nums[i]) - 1
            if nums[pos] < 0:
                return abs(nums[i])
            nums[pos] *= -1
        return -1

        # Binary Search
        # def binSearch(arr, target):
        #     l, r = 0, len(arr)
        #     while l <= r:
        #         m = (l + r) >> 1
        #         if arr[m] == target:
        #             return target
        #         elif arr[m] > target:
        #             r = m - 1
        #         else:
        #             l = m + 1
        #     return -1

        # nums.sort()
        # n = len(nums)

        # for i in range(n):
        #     num = nums[i]
        #     if binSearch(nums[i+1:], num) != -1:
        #         return num
            
        # return -1


        # Brute-force
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[j] == nums[i]:
        #             return nums[i]
        # return -1


        