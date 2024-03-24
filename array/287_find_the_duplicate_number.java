class Solution {
    public int findDuplicate(int[] nums) {
        for (int num : nums) {
            int pos = Math.abs(num);

            if (nums[pos - 1] < 0) return pos;
            nums[pos - 1] *= -1;
        }
        return -1;

        // int n = nums.length;
        // boolean[] seen = new boolean[n+1];

        // for (int num : nums) {
        //     if (seen[num - 1]) return num;
        //     seen[num - 1] = true;
        // }
        // return -1;
    }
}