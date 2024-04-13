class Solution {
    // public int twoSumLessThanK(int[] nums, int k) {
    //     Arrays.sort(nums);

    //     int left = 0, right = nums.length - 1;
    //     int res = -1;
    //     while (left < right) {
    //         int sum = nums[left] + nums[right];

    //         if (sum < k){
    //             res = Math.max(res, sum);
    //             left++;
    //         } else {
    //             right--;
    //         } 
    //     }
    //     return res;
    // }
    public int twoSumLessThanK(int[] nums, int k) {
        Arrays.sort(nums);
        int res = -1;

        for (int i = 0; i < nums.length - 1; i++) {
            int target = k - nums[i] - 1;
            int idx = Arrays.binarySearch(nums, i+1, nums.length, target);
            int j = idx >= 0 ? idx : ~idx;

            if (j == nums.length || nums[j] > target) j--;
            if (j > i) {
                res = Math.max(res, nums[i] + nums[j]);
            }
        }
        return res;
    }
}
