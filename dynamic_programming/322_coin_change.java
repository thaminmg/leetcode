class Solution {
    // BOTTOM UP -> O(S. N) + O(S)
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin > i) continue;
    
                dp[i] = Math.min(dp[i], 1 + dp[i - coin]);                       
            }
        }
        return (dp[amount] == amount + 1) ? - 1 : dp[amount];
    }
    
//      TOP DOWN -> O(S.N) + O(S)
//     int[] memo;
    
//     public int dp(int[] coins, int remaining) {
//         if (remaining < 0) return -1;
//         if (remaining == 0) return 0;
        
//         if (memo[remaining] != 0) return memo[remaining];
        
//         int minCoin = Integer.MAX_VALUE;
        
//         for (int coin : coins) {
//             int count = dp(coins, remaining - coin);
//             if (count == -1) continue;
//             minCoin = Math.min(minCoin, count + 1);
//         }
//         memo[remaining] = (minCoin == Integer.MAX_VALUE) ? - 1 : minCoin;
//         return memo[remaining];
//     }
    
//     public int coinChange(int[] coins, int amount) {
//         if (amount < 1) return 0;
//         memo = new int[amount + 1];
        
//         return dp(coins, amount);
//     }
}