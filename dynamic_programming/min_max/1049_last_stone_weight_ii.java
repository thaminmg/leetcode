class Solution {
    public int lastStoneWeightII(int[] stones) {
        int sum = 0;
        for (int stone : stones) {
            sum += stone;
        }

        Integer[][] dp = new Integer[stones.length][sum];
        return dfs(stones, 0, 0, 0, dp);
    }

    public int dfs(int[] stones, int curr, int sumL, int sumR, Integer[][] dp) {
        if (curr == stones.length) {
            return Math.abs(sumL - sumR);
        }
        if (dp[curr][sumL] != null) {
            return dp[curr][sumL];
        }

        dp[curr][sumL] = Math.min(
            dfs(stones, curr + 1, sumL + stones[curr], sumR, dp),
            dfs(stones, curr + 1, sumL, sumR + stones[curr], dp)
        );
        return dp[curr][sumL];
    }
}   

    
    