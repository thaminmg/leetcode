class Solution:
    def minOperations(self, s: str) -> int:
        startZero = 0
        startOne = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0':
                    startOne += 1
                else:
                    startZero += 1
            else:
                if s[i] == '0':
                    startZero += 1
                else:
                    startOne += 1

        return min(startZero, startOne)