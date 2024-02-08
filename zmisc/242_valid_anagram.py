from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # oglst = list()
        # if len(s) != len(t):
        #     return False
        # for i in range(len(s)):
        #     oglst.append(s[i])
        # print(oglst)
        # for i in range(len(s)):
        #     if t[i] in oglst:
        #         oglst.remove(t[i])
        #     else:
        #         return False
        # return True
        if len(s) != len(t):
            return False
        scounter = Counter(s)
        tcounter = Counter(t)
        # print(scounter)
        # print(tcounter)
        for i in scounter:
            if i not in tcounter or scounter[i] != tcounter[i]:
                return False
        return True


print(Solution().isAnagram('lesserafim', 'imfearless'))