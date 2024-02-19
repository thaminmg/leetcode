class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int left = 0, right = m - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (matrix[mid][0] == target) {
                return true;
            }
            else if (matrix[mid][0] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        int row = left - 1;
        if (row < 0) return false;
        
        int low = 0, high = n - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (matrix[row][mid] == target) {
                return true;
            }
            else if (matrix[row][mid] > target) {
                high = mid - 1; 
            } else {
                low = mid + 1;
            }
        }
        return false;
    }
}