class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if m < n: return -1
        if m == n: return 0 if haystack == needle else -1

        for i in range(m - n + 1):
            substr = haystack[i:i+n]
            if substr == needle:
                return i
        return -1
        