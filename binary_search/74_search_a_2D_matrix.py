class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(m*n)) + O(1)
        m, n = len(matrix), len(matrix[0])
        start, end = 0, (m * n) - 1
        while start <= end:
            mid = (start + end) // 2
            r, c = divmod(mid, n)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                end = mid - 1
            else: 
                start = mid + 1
        return False
    
        # O(log(m) + log(n)) + O(1)

        # def binarySearch(nums, target: int):
        #     start, end = 0, len(nums) - 1
        #     while start <= end:
        #         mid = (start + end) // 2
        #         if nums[mid] == target:
        #             return True
        #         elif nums[mid] > target:
        #             end = mid - 1
        #         else: 
        #             start = mid + 1
        #     return False

        # m, n = len(matrix), len(matrix[0])
        # top, bottom = 0, m - 1

        # while top <= bottom:
        #     mid = (top + bottom) // 2
        #     if matrix[mid][0] <= target <= matrix[mid][n - 1]:
        #         return binarySearch(matrix[mid], target)
        #     elif matrix[mid][0] > target:
        #         bottom = mid - 1
        #     else: 
        #         top = mid + 1
        # return False

        


        