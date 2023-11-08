class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        res = []
        *front, last = nums
        
        for perm in self.permuteUnique(front):
            for i in range(len(perm) + 1):
                combo = perm[:i] + [last] + perm[i:]
                if not combo in res:
                    res.append(combo)

        return res