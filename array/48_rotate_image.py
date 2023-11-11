class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:
            for offset in range(right - left):
                top, bottom = left, right

                temp = matrix[top][left + offset]
                matrix[top][left + offset] = matrix[bottom - offset][left]
                matrix[bottom - offset][left] = matrix[bottom][right - offset]
                matrix[bottom][right - offset] = matrix[top + offset][right]
                matrix[top + offset][right] = temp
            left += 1
            right -= 1
        