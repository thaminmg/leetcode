class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        positive = True
        negative = True
        for i in range(len(nums) - 1):
            positive &= nums[i] <= nums[i+1]
            negative &= nums[i] >= nums[i+1]
        return positive or negative 
        