class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) >> 1
            if target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low
        