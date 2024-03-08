class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        int m = matrix.length;
        int n = matrix[0].length;
        int top = 0;
        int left = 0;
        int bottom = m - 1;
        int right = n - 1;
        
        while (res.size() < m * n) {
            for (int col = left; col <= right; col++) {
                res.add(matrix[top][col]);
            }   
            
            for (int row = top+1; row <= bottom; row++) {
                res.add(matrix[row][right]);
            }
            
            if (top != bottom) {
                for (int col = right - 1; col >= left; col--) {
                    res.add(matrix[bottom][col]);
                }
            }
            
            if (left != right) {
                for (int row = bottom - 1; row > top; row--) {
                    res.add(matrix[row][left]);   
                }
            }
            top++;
            right--;
            left++;
            bottom--;
        }
        return res;
    }
}