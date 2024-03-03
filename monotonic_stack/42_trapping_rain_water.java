class Solution {
    public int trap(int[] height) {
        int res = 0;

        Stack<Integer> stack = new Stack<>();

        int curr = 0;
        while (curr < height.length) {
            while (!stack.empty() && height[curr] > height[stack.peek()]) {
                int topIdx = stack.pop();
                if (stack.empty()) break;

                int distance = curr - stack.peek() - 1;
                int boundedHeight = Math.min(height[curr], height[stack.peek()]) - height[topIdx];
                res += distance * boundedHeight;
            }
            stack.push(curr++);
        }

        return res;       
    }
}