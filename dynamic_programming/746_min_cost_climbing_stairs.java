class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] dp = new int[n + 1];
        
        for (int i = 2; i <= n; i++) {
            int oneStepCost = dp[i - 1] + cost[i - 1];
            int twoStepCost = dp[i - 2] + cost[i - 2];
            dp[i] = Math.min(oneStepCost, twoStepCost);
        }
        return dp[n];
    }
}