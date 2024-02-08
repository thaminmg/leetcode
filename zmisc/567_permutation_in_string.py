class Solution:
    def permute(self, word):
        if (len(word) == 1):
            return [word]
        permutations = Solution.permute(self, word[1:])
        pivot = word[0]
        result = []
        for p in permutations:
            for i in range(len(p) + 1):
                result.append(p[:i] + pivot + p[i:])
        return result
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lst = self.permute(s1)
        print(lst)
        for i in lst:
            if i in s2:
                return True
        return False


s1 = 'abcd'
s2 = 'dcda'
print(Solution().checkInclusion(s1,s2))