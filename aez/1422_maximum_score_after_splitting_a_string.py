class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(1, n):
            left = s[:i].count('0')
            right = s[i:].count('1')
            res = max(res, left+right)
        return res
        