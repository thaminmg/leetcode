class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        res = -1
        n = len(a)
        m = len(b)

        if n == m and a == b: return 1
        times = math.ceil(m / n) + 1
        k = 1
        while k <= times:
            if b in a * k:
                return k
            k += 1
        return res
        