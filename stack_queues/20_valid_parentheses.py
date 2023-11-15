class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if stack:
                    top = stack[-1]
                    if (top == '(' and ch == ')') or (top == '{' and ch == '}') or (top == '[' and ch == ']'):
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return True if not stack else False 
        
    # My accepted solution
    # Runtime: 32 ms, faster than 58.27% of Python3 online submissions for Valid Parentheses.
    # Memory Usage: 14.1 MB, less than 96.57% of Python3 online submissions for Valid Parentheses.    
    def isValid(self, s: str) -> bool:
        flag = False
        stack = []

        for i in range(len(s)):
            print(s[i])
            if (s[i] == "(" or s[i] == "{" or s[i] == "["):
                stack.append(s[i])
            elif len(stack) <= 0:
                flag = False
                break
            elif ((stack[-1] == "(" and s[i] == ")") or (stack[-1] == "{" and s[i] == "}") or (stack[-1] == "[" and s[i] == "]")):
                    stack.pop(-1) 
                    if len(stack) == 0:
                        flag = True        
            else:
                flag = False
                break

        if (len(stack) > 0):
            flag = False
        return flag

# Better solution
def isValid(self, s):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if stack:
                    top = stack[-1]
                    if i == ')' and top == '(' or i == '}' and top == '{' or i == ']' and top == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return False if stack else True
