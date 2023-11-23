class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        k = 0
        for ch in s:
            temp = s[:k+1]
            m = len(temp)
            times = math.ceil(n / m)
            news = temp * times
            if news == s and m <= n >> 1:
                return True
            k += 1
        return False