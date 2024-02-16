class Solution {
    public int[] sortArray(int[] nums) {
        if (nums.length <= 1) return nums;
        
        int pivot = nums.length / 2;
        
        int[] leftList = sortArray(Arrays.copyOfRange(nums, 0, pivot));
        int[] rightList = sortArray(Arrays.copyOfRange(nums, pivot, nums.length));
        
        return merge(leftList, rightList);
    }
    
    public int[] merge(int[] leftList, int[] rightList) {
        int[] res = new int[leftList.length + rightList.length];
        int leftCur = 0, rightCur = 0, resCur = 0;
        
        while (leftCur < leftList.length && rightCur < rightList.length) {
            if (leftList[leftCur] < rightList[rightCur]) {
                res[resCur++] = leftList[leftCur++];
            } else {
                res[resCur++] = rightList[rightCur++];
            }
        }
        
        while (leftCur < leftList.length) {
            res[resCur++] = leftList[leftCur++];
        }
        while (rightCur < rightList.length) {
            res[resCur++] = rightList[rightCur++];
        }
        return res;
    }
}