from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums]
        res = []
        *front, last = nums

        for perm in self.permute(front):
            for i in range(len(perm) + 1):
                permutation = perm[:i] + [last] + perm[i:]
                res.append(permutation)
        return res
        # return permutations(nums)

        