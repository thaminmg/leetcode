class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        s = s.strip()
        n = len(s)
        while n:
            if s[n-1] != ' ':
                res += 1
            else:
                break
            n -= 1
        return res
        