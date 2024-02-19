class Solution {
    int[][] mat;
    int tar;
    
    public boolean helper(int left, int up, int right, int down) {
        if (left > right || up > down) {
            return false;
        }
        else if (tar < mat[up][left] || tar > mat[down][right]) {
            return false;
        }
        
        int mid = left + (right - left) / 2;
        
        int row = up;
        while (row <= down && mat[row][mid] <= tar) {
            if (mat[row][mid] == tar) return true;
            row++;
        }
        
        return helper(left, row, mid - 1, down) || helper(mid+1, up, right, row - 1);
    }
    
    public boolean searchMatrix(int[][] matrix, int target) {
        mat = matrix;
        tar = target;
        
        if (matrix == null || matrix.length == 0) return false;
        
        return helper(0, 0, matrix[0].length - 1, matrix.length - 1);
    }
}