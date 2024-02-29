class Solution {
    // DC, O(n log n) - O (n^2), when array is in sorted order or same; TLE
    public int divideConquer(int[] heights, int start, int end) {
        if (start > end) {
            return 0;
        }
        
        int minIndex = start;
        for (int i = start; i <= end; i++) {
            if (heights[minIndex] > heights[i]) {
                minIndex = i;
            }
        }
        return Math.max(heights[minIndex] * (end - start + 1), 
                        Math.max(divideConquer(heights, start, minIndex - 1), divideConquer(heights, minIndex+1, end)));
    }
    
    public int largestRectangleArea(int[] heights) {
        return divideConquer(heights, 0, heights.length - 1);
    }
}