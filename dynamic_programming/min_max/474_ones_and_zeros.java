class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m + 1][n + 1];
        for (String str : strs) {
            int[] count = countZeroesOnes(str);

            for (int zeroes = m; zeroes >= count[0]; zeroes--) {
                for (int ones = n; ones >= count[1]; ones--) {
                    dp[zeroes][ones] = Math.max(1 + dp[zeroes-count[0]][ones-count[1]], dp[zeroes][ones]);
                }
            }
        }
        return dp[m][n];
    }

    public int[] countZeroesOnes(String s) {
        int[] res = new int[2];
        for (int i = 0; i < s.length(); i++) {
            res[s.charAt(i) - '0']++;
        }
        return res;
    }
}

// Resursive
class Solution {
    int[][][] dp;

    public int[] countZeroesOnes(String str) {
        int[] res = new int[2];
        for (int i = 0; i < str.length(); i++) {
            res[str.charAt(i) - '0']++;
        }
        return res;
    }

    public int dfs(String[] strs, int i, int m, int n) {
        if (i == strs.length) return 0;
        if (dp[i][m][n] != -1) return dp[i][m][n];

        int[] count = countZeroesOnes(strs[i]);
        int mCount = count[0], nCount = count[1];

        int taken = -1;
        if (m - mCount >= 0 && n - nCount >= 0) {
            taken = 1 + dfs(strs, i + 1, m - mCount, n - nCount);
        }
        int notTaken = dfs(strs, i + 1, m , n);

        return dp[i][m][n] = Math.max(taken, notTaken);
    }
    public int findMaxForm(String[] strs, int m, int n) {
        dp = new int[strs.length][m + 1][n + 1];
        for (int[][] twoD : dp) {
            for (int[] oneD : twoD) {
                Arrays.fill(oneD, -1);
            }
        }

        return dfs(strs, 0, m, n);
    }
}