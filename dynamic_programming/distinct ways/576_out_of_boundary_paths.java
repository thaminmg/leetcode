class Solution {
    final int MOD = 1000000007;

    public int dfs(int m, int n, int N, int x, int y, int[][][] memo) {
        if (x == m || y == n || x < 0 || y < 0) return 1;
        if (N == 0) return 0;

        if (memo[x][y][N] >= 0) return memo[x][y][N];

        int moves = ((dfs(m, n, N - 1, x - 1, y, memo) + dfs(m, n, N - 1, x + 1, y, memo)) % MOD + (dfs(m, n, N - 1, x, y - 1, memo) + dfs(m, n, N - 1, x, y + 1, memo)) % MOD) % MOD;

        return memo[x][y][N] = moves;
    }
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        int[][][] memo = new int[m][n][maxMove + 1];
        for (int[][] gp : memo) {
            for (int[] row : gp) {
                Arrays.fill(row, -1);
            }
        }
        return dfs(m, n, maxMove, startRow, startColumn, memo);
    }
}