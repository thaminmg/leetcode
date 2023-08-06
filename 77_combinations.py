class Solution:
    def combine(self, n: int, k: int) ->list[list[int]]:
        result = []
        def backtrack(start = 1, combo = []):
            if (len(combo) == k):
                result.append(combo.copy())        
                return
            for i in range(start, n + 1):
                combo.append(i)
                backtrack( i + 1, combo)
                combo.pop()
        backtrack()
        return result


n = 4
k = 2
print(Solution().combine(n, k))