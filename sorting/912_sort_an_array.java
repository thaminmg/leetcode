class Solution {
    public int[] sortArray(int[] nums) {
        for (int i = nums.length / 2 - 1; i >= 0; i--) {
            maxHeapify(nums, i, nums.length);
        }
        
        for (int i = nums.length - 1; i >= 0; i--) {
            int temp = nums[i];
            nums[i] = nums[0];
            nums[0] = temp;
            maxHeapify(nums, 0, i);    
        }
        return nums;
    }
    
    public void maxHeapify(int[] nums, int index, int heapSize) {
        int left = (2 * index) + 1;
        int right = (2 * index) + 2;
        int largest = index;
        
        if (left < heapSize && nums[left] > nums[largest]) {
            largest = left;
        }
        if (right < heapSize && nums[right] > nums[largest]) {
            largest = right;
        }
        if (largest != index) {
            int temp = nums[index];
            nums[index] = nums[largest];
            nums[largest] = temp;
            maxHeapify(nums, largest, heapSize);
        }
    }
}