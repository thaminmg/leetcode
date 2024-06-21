class Solution {
    int subsetSum = 0;

    public boolean dfs(int[] nums, Boolean[][] memo, int index, int currSum) {
        if (currSum == subsetSum) return true;
        if (index == nums.length || currSum > subsetSum) return false;
        
        if (memo[index][currSum] != null) {
            return memo[index][currSum];
        }

        boolean result = dfs(nums, memo, index + 1, currSum + nums[index]) || dfs(nums, memo, index + 1, currSum);
        return memo[index][currSum] = result;
    }
    public boolean canPartition(int[] nums) {
        int total = Arrays.stream(nums).sum();
        if (total % 2 != 0) return false;
        subsetSum = total / 2;

        Boolean[][] memo = new Boolean[nums.length + 1][subsetSum + 1];
        return dfs(nums, memo, 0, 0);
    }
}