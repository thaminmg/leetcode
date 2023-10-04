class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s)
        l = 0
        for r in range(len(words)):
            if s[r] == ' ' or r == len(s) - 1:
                left = l
                right = r - 1 if r != len(s) - 1 else r
                while left < right:
                    words[left], words[right] = words[right], words[left]
                    left += 1
                    right -= 1
                l = r + 1
        return ''.join(words)



        