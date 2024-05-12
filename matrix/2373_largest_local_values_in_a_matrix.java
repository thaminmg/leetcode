class Solution {

    public int findMax(int[][] grid, int i, int j) {
        int res = 0;
        for (int m = i; m < i + 3; m++) {
            for (int n = j; n < j + 3; n++) {
                res = Math.max(res, grid[m][n]);
            }
        }
        return res;
    }

    public int[][] largestLocal(int[][] grid) {
        int n = grid.length;
        int[][] res = new int[n - 2][n - 2];

        for (int i = 0; i < n - 2; i++) {
            for (int j = 0; j < n - 2; j++) {
                res[i][j] = findMax(grid, i, j);
            }
        }
        return res;
    }
}