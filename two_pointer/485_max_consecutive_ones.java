class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int res = 0;
        int temp = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                temp++;
            } else {
                res = Math.max(res, temp);
                temp = 0;
            }
        }
        res = Math.max(res, temp);
        return res;
    }
}