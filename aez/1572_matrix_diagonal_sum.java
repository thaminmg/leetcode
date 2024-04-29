class Solution {
    public int diagonalSum(int[][] mat) {
        int res = 0;

        int m = mat.length, n = mat[0].length - 1;
        for (int i = 0; i < m; i++) {
            if (i != n) {
                res += mat[i][i] + mat[i][n];
            } else {
                res += mat[i][i];
            }
            n--;
        }
        return res;
    }
}