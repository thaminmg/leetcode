class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotatePointer(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        if k > len(nums):
            k = k % len(nums)
        rotatePointer(nums, 0, len(nums) - 1)
        rotatePointer(nums, 0, k - 1)
        rotatePointer(nums, k, len(nums) - 1)

        