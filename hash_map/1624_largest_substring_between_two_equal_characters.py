class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        hset = {}

        for i in range(len(s)):
            if s[i] in hset:
                res = max(res, i - hset[s[i]] - 1)
            else:
                hset[s[i]] = i

        return res
        