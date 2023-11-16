class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def bubbleSort(nums, i):
            if i == 0:
                return
            else:
                for j in range(i):
                    if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                bubbleSort(nums, i - 1)

        bubbleSort(nums, len(nums) - 1)