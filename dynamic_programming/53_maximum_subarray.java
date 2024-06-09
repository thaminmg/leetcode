class Solution {
    public int maxSubArray(int[] nums) {
        int curr = 0, best = Integer.MIN_VALUE;

        for (int num : nums) {
            curr = Math.max(curr + num, num);
            best = Math.max(best, curr);
        }
        return best;
    }
}