class Solution {
    public int maxProfit(int[] prices, int fee) {
        int n = prices.length;
        int[] dp = new int[n], buyOrHold = new int[n];

        buyOrHold[0] = - prices[0];

        for (int i = 1; i < n; i++) {
            buyOrHold[i] = Math.max(buyOrHold[i - 1], dp[i - 1] - prices[i]);
            dp[i] = Math.max(dp[i - 1], buyOrHold[i - 1] + prices[i] - fee);
        }
        return dp[n - 1];
    }
}