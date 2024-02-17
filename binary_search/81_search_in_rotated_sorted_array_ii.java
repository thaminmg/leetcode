class Solution {
    public boolean search(int[] nums, int target) {
          int left = 0, right = nums.length - 1;

        while (left < right) {

            while (left < right && nums[left] == nums[left + 1]) {
                left += 1;
            }
            while (left < right && nums[right] == nums[right - 1]) {
                right -= 1;
            }
            
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return true;
            } else if (nums[mid] >= nums[left]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            } 
            else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
        }
        return left < nums.length && (nums[left] == target) ? true : false;
    }
}