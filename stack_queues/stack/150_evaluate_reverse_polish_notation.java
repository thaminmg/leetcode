class Solution {
    public int evalRPN(String[] tokens) {
        
        Stack<Integer> stack = new Stack<Integer>();
        String operators = "+-*/";
        
        int n = tokens.length;
        for (int i = 0; i < n; i++) {
            if (operators.indexOf(tokens[i]) != -1) {
                String operator = tokens[i];
                int operand2 = stack.pop();
                int operand1 = stack.pop();
                
                switch (operator) {
                    case "+":
                        stack.push(operand1 + operand2);
                        break;
                    case "-":
                        stack.push(operand1 - operand2);
                        break;
                    case "*":
                        stack.push(operand1 * operand2);
                        break;
                    case "/":
                        stack.push(operand1 / operand2);
                        break;
                    default:
                        stack.push(operand1);
                        stack.push(operand2);
                        break;
                }
            }
            else {
                stack.push(Integer.parseInt(tokens[i]));
            }
        }
        return stack.pop();
        
    }
}