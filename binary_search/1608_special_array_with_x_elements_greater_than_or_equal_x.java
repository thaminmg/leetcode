class Solution {
    public int helper(int[] nums, int val) {
        int left = 0, right = nums.length - 1;

        int index = nums.length; 
        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] >= val) {
                index = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return index;
    }

    public int specialArray(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;

        for (int i = 1; i <= n; i++) {
            int k = helper(nums, i);
            if (n - k == i) {
                return i;
            }
        }
        return -1;
    }
}