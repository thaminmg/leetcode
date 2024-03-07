class Solution {
    public int pivotIndex(int[] nums) {
        int total = 0;
        int[] sum = new int[nums.length];
        
        for (int i = 0; i < nums.length; i++) {
            total += nums[i];
            sum[i] = total;
        }
        for (int i = 0; i < nums.length; i++) {
            int left = sum[i] - nums[i];
            int right = total - sum[i];
            if (left == right) return i;
        }
        return -1;
    }
}