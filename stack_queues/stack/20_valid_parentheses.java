class Solution {
    public boolean isValid(String s) {
        String close = ")}]";
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char currChar = s.charAt(i);
            if (close.indexOf(currChar) != -1) {
                if (stack.empty()) return false;
                char top = stack.peek();
                if ((top == '(' && currChar == ')') || (top == '{' && currChar == '}') || (top == '[' && currChar == ']')) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(currChar);
            }
        }
        return stack.empty();
    }
}