class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        i = 0
        res = ''
        n = min(n1, n2)
        while i < n:
            res += word1[i] + word2[i]
            i += 1
        if n1 > i:
            res += word1[i:]
        if n2 > i:
            res += word2[i:]
        return res
        