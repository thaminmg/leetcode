class Solution {
    public boolean find132pattern(int[] nums) {

        Stack<Integer> stack = new Stack<>();
        int[] minimums = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                minimums[i] = 0;
            }
            else if (nums[i] < nums[minimums[i-1]]) {
                minimums[i] = i;
            } else {
                minimums[i] = minimums[i-1];
            }
        }

        for (int i = 0; i < nums.length; i++) {
            while (!stack.empty() && nums[stack.peek()] <= nums[i]) {
                stack.pop();
            }

            if (!stack.empty()) {
                if (nums[minimums[stack.peek()]] < nums[i]) return true;
            }
            stack.push(i);
        }
        return false;
    }
}