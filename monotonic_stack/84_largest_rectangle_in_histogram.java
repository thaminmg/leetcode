class Solution {
    
//     public int divideConquer(int[] heights, int start, int end) {
//         if (start > end) {
//             return 0;
//         }
        
//         int minIndex = start;
//         for (int i = start; i <= end; i++) {
//             if (heights[minIndex] > heights[i]) {
//                 minIndex = i;
//             }
//         }
//         return Math.max(heights[minIndex] * (end - start + 1), 
//                         Math.max(divideConquer(heights, start, minIndex - 1), divideConquer(heights, minIndex+1, end)));
//     }
    
    
    
    public int largestRectangleArea(int[] heights) {
        // return divideConquer(heights, 0, heights.length - 1);
        int n = heights.length;
        Stack<Integer> stack = new Stack<>();
        
        stack.push(-1);
        int res = 0;
        
        for (int i = 0; i < n; i++) {
            while (stack.peek() != - 1 && heights[stack.peek()] >= heights[i]) {
                int height = heights[stack.pop()];
                int width = i - stack.peek() - 1;
                res = Math.max(res, width * height);
            }   
            stack.push(i);
        }
        
        while (stack.peek() != - 1) {
            int height = heights[stack.pop()];
            int width = n - stack.peek() - 1;
            res = Math.max(res, width * height);
        }
        return res;
    }
}