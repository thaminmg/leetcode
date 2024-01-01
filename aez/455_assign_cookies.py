class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        idx = 0
        while idx < len(s) and res < len(g):
            if s[idx] >= g[res]:
                res += 1
            idx += 1
        return res
        