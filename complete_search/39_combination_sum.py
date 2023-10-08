class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, cur, target):
            if target == 0:
                return [cur]
            res = []
            for j in range(i, len(candidates)):
                if target - candidates[j] >= 0:
                    res += dfs(j, cur + [candidates[j]], target-candidates[j])
            return res
        return dfs(0, [], target)
        # res = []
        # subset = []
        # total = 0
        # def dfs(n: int, total: int):
        #     if total >= target or n >= len(candidates):
        #         if total == target:
        #             res.append(subset.copy())
        #         return
        #     subset.append(candidates[n])
        #     dfs(n, total + candidates[n])
        #     subset.pop()
        #     dfs(n+1, total)
        # dfs(0, total)

        # return res
        