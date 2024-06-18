class Solution {
    public int minSteps(int n) {
        int[] memo = new int[n + 1];

        Arrays.fill(memo, -2);
        memo[n] = 0;
        return dfs(n, 1, memo);
    }

    public int dfs(int n, int len, int[] memo) {
        if (memo[len] != -2) {
            return memo[len];
        }
        int res = Integer.MAX_VALUE;

        int copied = len, pastes = 0;
        while (len + copied <= n) {
            len += copied;
            pastes++;

            int remain = dfs(n, len, memo);
            
            if (remain != -1) {
                res = Math.min(res, pastes + remain);
            }
        }
        memo[len] = res == Integer.MAX_VALUE ? - 1 : res + 1;
        return memo[len];
    }
}