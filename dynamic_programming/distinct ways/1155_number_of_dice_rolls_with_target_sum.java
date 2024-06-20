class Solution {
    final int MOD = 1000000007;
    public int dfs(int n, int k, int target, Integer[][] memo, int index, int currSum) {
        if (index == n) {
            return currSum == target ? 1 : 0;
        }

        if (memo[index][currSum] != null) {
            return memo[index][currSum];
        }

        int ways = 0;
        for (int i = 1; i <= Math.min(k, target - currSum); i++) {
            ways = (ways + dfs(n, k, target, memo, index + 1, currSum + i)) % MOD;
        }
        return memo[index][currSum] = ways;
    }
    public int numRollsToTarget(int n, int k, int target) {
        Integer[][] memo = new Integer[n + 1][target + 1];
        return dfs(n, k, target, memo, 0, 0);
    }
}

class Solution {
    public int numRollsToTarget(int n, int k, int target) {
        final int MOD = 1000000007;

        int[][] dp = new int[n + 1][target + 1];
        dp[n][target] = 1;

        for (int index = n - 1; index >= 0; index--) {
            for (int currSum = 0; currSum <= target; currSum++) {
                int ways = 0;
                for (int face = 1; face <= Math.min(k, target - currSum); face++) {
                    ways = (ways + dp[index + 1][currSum + face]) % MOD;
                }
                dp[index][currSum] = ways;
            }
        }
        return dp[0][0];
    }
}