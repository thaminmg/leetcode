class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] answer = new int[n];
        Stack<Integer> stack = new Stack<Integer>();

        for (int i = 0; i < n; i++) {
            int currDay = temperatures[i];
            
            while (!stack.empty() && temperatures[stack.peek()] < currDay) {
                int prevDayIdx = stack.pop();
                answer[prevDayIdx] = i - prevDayIdx;
            }
            stack.push(i);
        }
        return answer;
    }
}