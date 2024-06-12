class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int[][] dp = new int[m][n];

        for (int j = 0; j < n; j++) {
            dp[0][j] = matrix[0][j];
        }

        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dp[i][j] = matrix[i][j] + Math.min(dp[i - 1][j],
                    Math.min(
                        dp[i - 1][Math.max(0, j - 1)],
                        dp[i - 1][Math.min(n - 1, j + 1)]
                    )
                );
            }
        }
        
        int res = Integer.MAX_VALUE;
        for (int num : dp[m - 1]) {
            res = Math.min(res, num);
        }
        return res;
    }
}