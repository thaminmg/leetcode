class Solution {

    public int binarySearchLeftRight(int[] nums, int target, boolean isRight) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;


            if (nums[mid] == target) {
                if (isRight) {
                    if (mid == right || nums[mid+1] != target) return mid;
                    left = mid + 1;
                } else {
                    if (mid == left || nums[mid-1] != target) return mid;
                    right = mid - 1;
                }
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            
        }
        return -1;
    }

    public int[] searchRange(int[] nums, int target) {
        
        int left = binarySearchLeftRight(nums, target, false);
        int right = binarySearchLeftRight(nums, target, true);

        return new int[] {left, right};
    }
}