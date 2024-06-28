class Solution {
    final int MOD = 1000000007;

    public int dfs(int[][] board, int[][] memo, int count, int no) {
        if (count == 0) return 1;
        if (memo[count][no] != 0) return memo[count][no];

        int ans = 0;
        for (int nextNo : board[no]) {
            ans = (ans + dfs(board, memo, count - 1, nextNo)) % MOD;
        }
        return memo[count][no] = ans;
    }
    public int knightDialer(int n) {
        int[][] board = {
            {4, 6},
            {6, 8},
            {7, 9},
            {4, 8},
            {3, 9, 0},
            {},
            {1, 7, 0},
            {2, 6},
            {1, 3},
            {2, 4}
        };
        int[][] memo = new int[n + 1][10];
        
        int res = 0;
        for (int num = 0; num <= 9; num++) {
            res = (res + dfs(board, memo, n - 1, num)) % MOD;
        }
        return res;
    }
}