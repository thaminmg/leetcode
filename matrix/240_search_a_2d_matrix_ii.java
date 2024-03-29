class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length - 1, col = 0;

        while (row >= 0 && col <= matrix[0].length - 1) {
            if (matrix[row][col] > target) {
                row--;
            } else if (matrix[row][col] < target) {
                col++;
            } else {
                return true;
            }
        }
        return false;
    }
}