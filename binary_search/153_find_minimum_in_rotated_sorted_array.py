class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        left, right = 0, len(nums) - 1
        
        if nums[right] > nums[left]: return nums[left]
        
        while left < right:
            mid = (left + right) >> 1
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid
        return left
        
            
        
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         start, end = 0, len(nums) - 1
#         res = float('inf')
#         while start <= end:
#             mid = (start + end) // 2
#             res = min(res, nums[mid])

#             if nums[mid] > nums[end]:
#                 start = mid + 1
#             else:
#                 end = mid - 1

#         return res
            
        