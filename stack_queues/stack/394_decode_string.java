class Solution {
    
    public String decodeString(String s) {
        String digits = "0123456789";
        
        Stack<Character> stack = new Stack<>();
        String answer = "";
       
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ']') {
                String temp = "";
             
                while (stack.peek() != '[') {                    
                    temp = stack.pop() + temp;
                }
                stack.pop(); // '['
                String k = "";
                while (!stack.empty() && digits.indexOf(stack.peek()) != -1) {
                    k = stack.pop() + k;
                }
                int kTimes = Integer.parseInt(k);
                String res = temp.repeat(kTimes);
                
                res.chars().forEach(c -> stack.push((char)c));
            } else {
                stack.push(s.charAt(i));
            }
        }
        while (!stack.empty()) {
            answer = stack.pop() + answer;
        }
        return answer;
    }
}