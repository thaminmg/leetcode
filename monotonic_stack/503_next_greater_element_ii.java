class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int[] res = new int[nums.length];
        Stack<Integer> stack = new Stack<>();
       
        for (int i = 0; i < nums.length; i++) {
            while (!stack.empty() && nums[stack.peek()] < nums[i]) {
                int topIndex = stack.pop();
                res[topIndex] = nums[i];
            }
            stack.push(i);
        }

        for (int i = 0; i < nums.length; i++) {
            while (!stack.empty() && nums[stack.peek()] < nums[i]) {
                int topIndex = stack.pop();
                res[topIndex] = nums[i];
            }
        }

        while(!stack.empty()) {
            res[stack.pop()] = -1;
        }

        return res;
    }
}