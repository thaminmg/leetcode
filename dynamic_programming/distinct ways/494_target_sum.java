class Solution {
    int total = 0;

    public int dfs(int[] nums, int target, int[][] memo, int index, int currSum) {
        if (index == nums.length) {
            return currSum == target ? 1 : 0;
        }

        if (memo[index][currSum + total] != Integer.MIN_VALUE) {
            return memo[index][currSum  + total];
        }

        int addition = dfs(nums, target, memo, index + 1, currSum + nums[index]);
        int subtraction = dfs(nums, target, memo, index + 1, currSum - nums[index]);

        return memo[index][currSum  + total] = addition + subtraction;
    }
    
    public int findTargetSumWays(int[] nums, int target) {
        for (int num : nums) {
            total += num;
        }
        int[][] memo = new int[nums.length][2 * total + 1];
        for (int[] row : memo) {
            Arrays.fill(row, Integer.MIN_VALUE);
        }
        return dfs(nums, target, memo, 0, 0);
    }
}