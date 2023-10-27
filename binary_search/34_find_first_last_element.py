class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = self.searchLeftmost(nums, target)
        if x == -1:
            return [-1, -1]
        else:
            return [x, self.searchRightmost(nums, target)]
    
    def searchLeftmost(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        candidate = -1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] < target:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                candidate = mid
                high = mid - 1
        return candidate

    def searchRightmost(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        candidate = -1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] < target:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                candidate = mid
                low = mid + 1
        return candidate
    
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         def binary_search(nums, target, left):
#             low, high = 0, len(nums) - 1
#             index = -1
#             while low <= high:
#                 mid = (low + high) // 2
#                 if nums[mid] == target:
#                     index = mid
#                     if left:
#                         high = mid - 1
#                     else:
#                         low = mid + 1
#                 elif nums[mid] < target:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#             return index

#         left_index = binary_search(nums, target, left=True)
#         right_index = binary_search(nums, target, left=False)

#         return [left_index, right_index]