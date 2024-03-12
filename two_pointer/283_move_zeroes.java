class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                continue;
            }
            nums[k++] = nums[i];
        }
        for (; k < nums.length; k++) {
            nums[k] = 0;
        }
    }
}