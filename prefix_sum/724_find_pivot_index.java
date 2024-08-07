class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0, currSum = 0;

        for (int num : nums) sum += num;

        for (int i = 0; i < nums.length; i++) {
            if (currSum == sum - currSum - nums[i]) {
                return i;
            }
            currSum += nums[i];
        }
        return -1;
    }
}