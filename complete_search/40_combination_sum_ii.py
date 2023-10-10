class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        subset = []
        def dfs(i, total):
            if i > n - 1 or total >= target:
                if total == target:
                    res.append(subset.copy())
                return
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            subset.pop()
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)
        dfs(0, 0)
        return res
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         candidates.sort()

#         res = []

#         def backtrack(cur, pos, target):
#             if target == 0:
#                 res.append(cur.copy())
#                 return
#             if target <= 0:
#                 return

#             prev = -1
#             for i in range(pos, len(candidates)):
#                 if candidates[i] == prev:
#                     continue
#                 cur.append(candidates[i])
#                 backtrack(cur, i + 1, target - candidates[i])
#                 cur.pop()
#                 prev = candidates[i]

#         backtrack([], 0, target)
#         return res
