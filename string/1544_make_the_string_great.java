class Solution {
    public String makeGood(String s) {
        // Two Pointer
        if (s.length() ==0 || s.length() == 1) return s;

        StringBuilder sb = new StringBuilder();
        int i = 0;
        sb.append(s);

        while (i < sb.length() - 1) {
            char leftChar = sb.charAt(i);
            char rightChar = sb.charAt(i+1);

            if (Math.abs(leftChar - rightChar) == 32) {
                sb.delete(i, i+2);
                if (i > 0) i--;
            } else {
                i++;
            }
        }
        return sb.toString();
        // O(n) + O(n)

        // Stack
        // Stack<Character> stack = new Stack<>();

        // for (char c : s.toCharArray()) {
        //     if (!stack.isEmpty() && Math.abs(stack.peek() - c) == 32) {
        //         stack.pop();
        //     } else {
        //         stack.add(c);
        //     }
        // }
        // StringBuilder sb = new StringBuilder();
        // while (!stack.isEmpty()) {
        //     sb.append(stack.pop());
        // }
        // return sb.reverse().toString();
        // O(n) + O(n)

        // Recursion
        // int n = s.length();
        // for (int i = 0; i < n - 1; i++) {
        //     if (Character.toUpperCase(s.charAt(i)) == s.charAt(i+1)) {
        //         return makeGood(s.substring(0,i) + s.substring(i+2)); 
        //     }
        // }
        // return s;    
        // O(n^2) + O(n^2)
    }
}