class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if len(token) == 1 and token in operators:
                operand1 = stack.pop()
                operand2 = stack.pop()
                result = None
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand2 - operand1
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    result = int(operand2 / operand1)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()
        