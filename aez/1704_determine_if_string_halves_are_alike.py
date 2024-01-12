class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) >> 1
        s1, s2 = s[: mid], s[mid:]
        res1, res2 = 0, 0

        for ch in s1:
            if ch in 'aeiouAEIOU': res1 += 1
        for ch in s2:
            if ch in 'aeiouAEIOU': res2 += 1
        
        return res1 == res2     