class Solution {
    public int minOperations(String[] logs) {
        Stack<String> stack = new Stack();

        for (int i = 0; i < logs.length; i++) {
            String log = logs[i];
            if (log.equals("../")) {
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (!log.equals("./")) {
                stack.push(log);
            }
        }
        return stack.size();
    }
}