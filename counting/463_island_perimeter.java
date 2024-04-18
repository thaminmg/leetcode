class Solution {
    public int islandPerimeter(int[][] grid) {
        int m = grid.length, n = grid[0].length;

        int up, down, left, right;
        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) continue;
                
                if (i == 0) {
                    up = 0;
                } else {
                    up = grid[i - 1][j];
                }

                if (j == 0) {
                    left = 0;
                } else {
                    left = grid[i][j-1];
                }

                if (i == m - 1) {
                    down = 0;
                } else {
                    down = grid[i+1][j];
                }

                if (j == n - 1) {
                    right = 0;
                } else {
                    right = grid[i][j+1];
                }

                res += 4 - (up + down + left + right);
            }
        }
        return res;
    }
}