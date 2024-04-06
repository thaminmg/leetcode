class Solution {
    public String minRemoveToMakeValid(String s) {
        // s = "lee(t(c)o)de)" -> "lee(t(c)o)de"
        // s = "))((" -> ""
        Stack<Integer> stack = new Stack<>();
        Set<Integer> stackIdx = new HashSet<>();

        for (int i = 0; i < s.length(); i++) {
            char temp = s.charAt(i);
            if (temp == '(') {
                stack.push(i);
            } else if (temp == ')'){
                if (stack.isEmpty()) {
                    stackIdx.add(i);
                } else {
                    stack.pop();
                }
            }
        }
        while (!stack.isEmpty()) {
            stackIdx.add(stack.pop());
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (!stackIdx.contains(i)) {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
        // O(n) + O(n)
    }
}