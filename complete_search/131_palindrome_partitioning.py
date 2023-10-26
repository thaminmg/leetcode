class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []
        def isPalindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r -1
            return True

        def dfs(i):
            if i == len(s):
                res.append(parts.copy())
                return
            for j in range(i, len(s)):
                print(s[i: j+1])
                if isPalindrome(s, i, j):
                    parts.append(s[i: j + 1])
                    dfs(j + 1)
                    parts.pop()
        
        dfs(0)
        return res

    
        