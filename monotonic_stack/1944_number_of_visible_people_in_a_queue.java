class Solution {
    public int[] canSeePersonsCount(int[] heights) {
        int[] res = new int[heights.length];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < heights.length; i++) {
            while (!stack.empty() && heights[stack.peek()] <= heights[i]) {
                int topIndex = stack.pop();
                res[topIndex] += 1;
            }
            if (!stack.empty()) {
                res[stack.peek()] += 1;
            }

            stack.push(i);
        }
        return res;
    }
}