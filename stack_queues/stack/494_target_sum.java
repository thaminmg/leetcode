class Solution {
    private int res = 0;
    
    public int findTargetSumWays(int[] nums, int target) {
        dfs(nums, 0, 0, target);
        return res;
    }
    
    private void dfs(int[] nums, int i, int sum, int target) {
        if (i == nums.length) {
            if (sum == target) {
                res++;
            }
            return;
        }
        
        dfs(nums, i + 1, sum + nums[i], target);
        dfs(nums, i + 1, sum - nums[i], target);
    }
}