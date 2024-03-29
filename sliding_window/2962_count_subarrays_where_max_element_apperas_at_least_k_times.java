class Solution {
    public long countSubarrays(int[] nums, int k) {
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            max = Math.max(max, num);
        }

        long res = 0;
        int left = 0, count = 0;

        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == max) count++;

            while (count == k) {
                if (nums[left] == max) count--;
                left++;
            }
            res += left;
            
        }

        return res;
    }
}