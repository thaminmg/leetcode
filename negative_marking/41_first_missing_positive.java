class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            if (nums[i] < 1 || nums[i] > n) {
                nums[i] = n + 1;
            }
        }

        for (int i = 0; i < n; i++) {
            int temp = Math.abs(nums[i]);
            if (temp > n) continue;
            temp -= 1;
            if (nums[temp] > 0) {
                nums[temp] *= -1;
            }
        }

        for (int i = 0; i < n; i++) {
            if (nums[i] >= 0) {
                return i + 1;
            }
        }
        return n + 1;
    }
}