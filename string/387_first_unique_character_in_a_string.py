class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = -1
        fset = Counter(s)
        for idx in range(len(s)):
            if fset[s[idx]] == 1:
                return idx
        return res
        