class Solution {
    public int maxProfit(int[] prices) {
        int curr = 0, best = 0;
        
        for (int i = 1; i < prices.length; i++) {
            curr = Math.max(0, curr += prices[i] - prices[i - 1]);
            best = Math.max(curr, best);
        }
        return best;
    }
}