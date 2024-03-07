class Solution {
    public int dominantIndex(int[] nums) {
        int largest = 0;
        int secondLargest = 0;
        int index = -1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > largest) {
                secondLargest = largest;
                largest = nums[i];
                index = i;
            } else if (nums[i] > secondLargest) {
                secondLargest = nums[i];
            }
        }
        return (largest >= 2 * secondLargest) ? index : - 1;    
    }
}