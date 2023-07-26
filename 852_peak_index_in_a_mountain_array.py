class Solution:

    def bin_search(self, arr: list[int], low: int, high: int, target: int) -> int:
        if low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                if arr[mid + 1] < arr[mid]:
                    return self.bin_search(arr, mid + 1, high, target)
                else:
                    return self.bin_search(arr, low, mid - 1, target)
            else:
                if arr[mid + 1] < arr[mid]:
                    return self.bin_search(arr, low, mid - 1, target)
                else:
                    return self.bin_search(arr, mid + 1, high, target)
        else:
            return -1

    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        high = max(arr)
        print(f'high {high}')
        return self.bin_search(arr, 0, len(arr) - 1, high)

arr = [24,69,100,99,79,78,67,36,26,19]
print(Solution().peakIndexInMountainArray(arr))