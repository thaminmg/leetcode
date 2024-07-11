class Solution {
    public void reverseString(StringBuilder sb, int left, int right) {
        while (left < right) {
            char temp = sb.charAt(left);
            sb.setCharAt(left++, sb.charAt(right));
            sb.setCharAt(right--, temp);
        }
    }

    public String reverseParentheses(String s) {
        Stack<Integer> stack = new Stack();
        StringBuilder res = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(res.length());
            } else if (c == ')') {
                int start = stack.pop();
                reverseString(res, start, res.length() - 1);
            } else {
                res.append(c);
            }
        }
        return res.toString();
    }
}