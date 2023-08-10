class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) -1

        while left <= right:
            # check duplicates
            while (left < right and nums[left] == nums[left + 1]):
                left += 1
            while (left < right and nums[right] == nums[right - 1]):
                right -= 1

            # bin search
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
    
nums = [1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]
target = 13
print(Solution().search(nums, target))