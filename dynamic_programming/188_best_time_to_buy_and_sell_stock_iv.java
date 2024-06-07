class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        int[][][] dp = new int[n + 1][k + 1][2];
        
        for (int i = n - 1; i >= 0; i--) {
            for (int remaining = 1; remaining <= k; remaining++) {
                for (int holding = 0; holding < 2; holding++) {
                    int doNothing = dp[i + 1][remaining][holding];
                    int doSomething;
                    
                    if (holding == 1) {
                        doSomething = prices[i] + dp[i + 1][remaining - 1][0];
                    } else {
                        doSomething = - prices[i] + dp[i + 1][remaining][1];
                    }
                    dp[i][remaining][holding] = Math.max(doNothing, doSomething);
                }
            }
        }
        
        return dp[0][k][0];
    }
}