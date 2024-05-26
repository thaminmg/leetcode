class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int left = 0, right = n - 1;
        
        for (int i = n - 1; i >= 0; i--) {
            int temp;
            if (Math.abs(nums[left]) < Math.abs(nums[right])) {
                temp = Math.abs(nums[right--]);
            } else {
                temp = Math.abs(nums[left++]);
            }
            res[i] = temp * temp;
        }
        return res;
    }
}