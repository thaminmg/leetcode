class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] leftProduct = new int[n];
        int[] rightProduct = new int[n];

        int currLeft = 1;
        for (int i = 0; i < n; i++) {
            leftProduct[i] = currLeft;
            currLeft *= nums[i];
        }

        int currRight = 1;
        for (int i = n - 1; i >= 0; i--) {
            rightProduct[i] = currRight;
            currRight *= nums[i];
        }

        for (int i = 0; i < n; i++) {
            nums[i] = leftProduct[i] * rightProduct[i];
        }
        return nums;
    }
}