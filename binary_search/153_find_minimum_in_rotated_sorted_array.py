class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        res = float('inf')
        while start <= end:
            mid = (start + end) // 2
            res = min(res, nums[mid])

            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1

        return res
            
        