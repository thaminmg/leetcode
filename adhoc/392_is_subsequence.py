class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)
        nt = len(t)
        if n > nt or (nt == 0 and n != 0):
            return False
        if n == 0 or (n == 0 and nt == 0):
            return True
        for ch in t:
            if i < n and ch == s[i]:
                i+= 1
        if i == n:
            return True
        return False
        