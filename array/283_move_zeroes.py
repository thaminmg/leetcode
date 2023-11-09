class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0

        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
        # index = 0

        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[index] = nums[i]
        #         index += 1
            
        # for j in range(index, len(nums)):
        #     nums[j] = 0
        