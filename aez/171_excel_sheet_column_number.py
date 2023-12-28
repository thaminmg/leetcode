class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        n = len(columnTitle)

        for i in range(n):
            res = res * 26
            res += (ord(columnTitle[i]) - ord('A') + 1)

        return res

        