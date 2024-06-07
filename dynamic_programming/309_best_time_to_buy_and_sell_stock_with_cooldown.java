class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        
        int dp[] = new int[n + 2];
        
        for (int i = n - 1; i >= 0; i--) {
            int buyAndSell = 0;
            for (int sell = i + 1; sell < n; sell++) {
                buyAndSell = Math.max(buyAndSell, (prices[sell] - prices[i]) + dp[sell + 2]);
            }
            
            int doNothing = dp[i + 1];
            
            dp[i] = Math.max(buyAndSell, doNothing);
        }
    
        return dp[0];
    }
}