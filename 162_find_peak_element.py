class Solution:
    def binSearch(self, arr: list[int], low: int, high: int, target: int) -> int:
        if low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                if arr[mid+1] < arr[mid]:
                    return self.binSearch(arr, mid+1, high, target)
                else:
                    return self.binSearch(arr, low, mid - 1, target)
            else:
                if arr[mid+1] < arr[mid]:
                    return self.binSearch(arr, low, mid - 1, target)
                else:
                    return self.binSearch(arr, mid+1, high, target)

        else:
            return -1

    def findPeakElement(self, nums: list[int]) -> int:
        return self.binSearch(nums, 0, len(nums) - 1, max(nums))


nums = [3,1,2]
print(Solution().findPeakElement(nums))