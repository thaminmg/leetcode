class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> res = new ArrayList<>();
        res.add(nums[0]);
        
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > res.get(res.size() - 1)) {
                res.add(nums[i]);
            } else {
                int j = binarySearch(res, nums[i]);
                res.set(j, nums[i]);
            }
        }
        return res.size();
    }
    
    public int binarySearch(List<Integer> arr, int num) {
        int left = 0, right = arr.size() - 1;
        int mid = 0;
        
        while (left < right) {
            mid = left + (right - left) / 2;
            
            if (arr.get(mid) >= num) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
}