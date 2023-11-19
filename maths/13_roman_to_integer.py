class Solution:
    def romanToInt(self, s: str) -> int:
        hset = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        for i in range(len(s) - 1):
            if hset[s[i]] < hset[s[i+1]]:
                res -= hset[s[i]]
            else:
                res += hset[s[i]]
        return res + hset[s[-1]]