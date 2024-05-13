class Solution {
    public int[][] generateMatrix(int n) {
        int[][] res = new int[n][n];
        int rowStart = 0, rowEnd = n - 1;
        int colStart = 0, colEnd = n - 1;
        int element = 1;
        while (rowStart <= rowEnd && colStart <= colEnd) {
            for (int j = colStart; j <= colEnd; j++) {
                res[rowStart][j] = element++;
            };

            for (int i = rowStart + 1; i <= rowEnd; i++) {
                res[i][colEnd] = element++;
            }

            for (int j = colEnd - 1; j >= colStart; j--) {
                res[rowEnd][j] = element++;
            }

            for (int i = rowEnd - 1; i > rowStart; i--) {
                res[i][colStart] = element++;
            }

            rowStart++;
            rowEnd--;
            colStart++;
            colEnd--;
        }
        return res;
    }
}