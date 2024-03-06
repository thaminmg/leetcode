class Solution {
    public String smallestSubsequence(String s) {
        Stack<Character> stack = new Stack<>();
        int[] counts = new int[26];
        boolean[] visited = new boolean[26];

        for (char c : s.toCharArray()) counts[c - 'a']++;

        for (char c : s.toCharArray()) {
            counts[c - 'a']--;

            if (visited[c - 'a']) continue;

            while (!stack.empty() && stack.peek() > c && counts[stack.peek() - 'a'] > 0) {
                char top = stack.pop();
                visited[top - 'a'] = false;
            }
            stack.push(c);
            visited[c - 'a'] = true;
        }

        StringBuilder str = new StringBuilder(stack.size());
        for (char c : stack) str.append(c);
        return str.toString();
    }
}