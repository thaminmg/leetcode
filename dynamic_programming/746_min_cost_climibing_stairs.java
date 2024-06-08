class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int oneCost = 0;
        int twoCost = 0;

        for (int i = 2; i <= cost.length; i++) {
            int temp = oneCost;
            oneCost = Math.min(oneCost + cost[i - 1], twoCost + cost[i - 2]);
            twoCost = temp;
        }
        return oneCost;
    }
}