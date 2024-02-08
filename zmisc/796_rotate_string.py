class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) < len(s):
            return False
        x = s + s
        y = goal
        return y in x
print(Solution().rotateString('aa', 'a'))