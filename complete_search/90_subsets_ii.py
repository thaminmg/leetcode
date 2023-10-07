class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # subset = []
        # def search(n: int):
        #     if (n == len(nums)):
        #         temp = []
        #         for idx in subset:
        #             temp.append(nums[idx])
        #         newtemp = sorted(temp)
        #         if newtemp not in res:
        #             res.append(newtemp)
        #         return
        #     else:
        #         search(n + 1)
        #         subset.append(n)
        #         search(n + 1)
        #         subset.pop()
        # search(0)
        # return res

          # using bit masking
        res = []
        n = len(nums)

        for i in range(2 ** n):
            subset = []
            for j in range(n):
                if (i & 1 << j != 0):
                    subset.append(nums[j])
            temp = sorted(subset)
            if temp not in res:
                res.append(temp)
        return res
        