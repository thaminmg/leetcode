class Solution {
    private final int NUM_DIGITS = 10;
    
    public void helper(int[] nums, int placeValue){
        int[] counts = new int[NUM_DIGITS];
        for (int num : nums) {
            int current = num / placeValue;
            counts[current % NUM_DIGITS] += 1;
        }
        
        int startingIndex = 0;
        for (int i = 0; i < counts.length; i++) {
            int count = counts[i];
            counts[i] = startingIndex;
            startingIndex += count;
        }
        
        int[] sortedArr = new int[nums.length];
        for (int num : nums) {
            int current = num / placeValue;
            sortedArr[counts[current % NUM_DIGITS]] = num;
            counts[current % NUM_DIGITS] += 1;
        }
        
        for (int i = 0; i < nums.length; i++) {
            nums[i] = sortedArr[i];
        }
    }
    
    public int[] radixSort(int[] nums) {
        int maxNum = Integer.MIN_VALUE;
        
        for (int num : nums) {
            if (num > maxNum) {
                maxNum = num;
            }
        }
        int placeValue = 1;
        while( maxNum / placeValue > 0) {
            helper(nums, placeValue);
            placeValue *= 10;
        }
        return nums;
    }
    
    public int maximumGap(int[] nums) {
    
        int[] sortedNums = radixSort(nums);
       
        int res = 0;
        for (int i = 1; i < nums.length; i++) {
            res = Math.max(res, sortedNums[i] - sortedNums[i-1]);
        }
        return res;
    }
}