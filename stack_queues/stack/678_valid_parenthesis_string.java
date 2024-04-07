class Solution {
    public boolean checkValidString(String s) {
        Stack<Integer> stack = new Stack<>();
        Stack<Integer> asStack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(') {
                stack.push(i);
            } else if (c == ')') {
                if (!stack.isEmpty()) {
                    stack.pop();
                } else if (!asStack.isEmpty()) {
                    asStack.pop();
                } else {
                    return false;
                }
            } else {
                asStack.push(i);
            }
        }

        while (!stack.isEmpty() && !asStack.isEmpty()) {
            if (stack.pop() > asStack.pop()) return false;
        }    

        return stack.isEmpty();
    }
}