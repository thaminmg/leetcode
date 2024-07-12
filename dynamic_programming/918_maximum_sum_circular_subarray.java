class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int currMax = 0, currMin = 0;
        int globalMax = nums[0], globalMin = nums[0];
        int total = 0;
        boolean allNegative = true;
        
        for (int num : nums) {
            total += num;

            currMax = Math.max(currMax + num, num);
            globalMax = Math.max(currMax, globalMax);

            currMin = Math.min(currMin + num, num);
            globalMin = Math.min(currMin, globalMin);

            if (num > 0) {
                allNegative = false;
            }
        }

        if (allNegative) {
            return globalMax;
        }

        return Math.max(globalMax, total - globalMin);
    }
}