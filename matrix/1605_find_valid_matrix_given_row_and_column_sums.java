class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        int m = rowSum.length, n = colSum.length;
        int[][] res = new int[m][n];

        int[] currRowSum = new int[m];
        int[] currColSum = new int[n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = Math.min(
                    rowSum[i] - currRowSum[i],
                    colSum[j] - currColSum[j]
                );

                currRowSum[i] += res[i][j];
                currColSum[j] += res[i][j];
            }
        }
        return res;
    }
}