class Solution:
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
