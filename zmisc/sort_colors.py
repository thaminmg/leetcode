class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        RED, WHITE, BLUE = range(3)
        pivot = WHITE
        smaller, equal, larger = 0, 0, len(nums)

        while equal < larger:
            if nums[equal] < pivot:
                nums[smaller], nums[equal] = nums[equal], nums[smaller]
                smaller, equal = smaller + 1, equal + 1
            elif nums[equal] == pivot:
                equal += 1
            else:
                larger -= 1
                nums[larger], nums[equal] = nums[equal], nums[larger]
