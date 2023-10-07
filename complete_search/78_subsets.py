class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # using recursion
        res = []
        subset = []
        def search(n: int):
            if (n == len(nums)):
                temp = []
                for idx in subset:
                    temp.append(nums[idx])
                res.append(temp)
                return
            else:
                search(n + 1)
                subset.append(n)
                search(n + 1)
                subset.pop()
        search(0)
        return res

        # using bit masking
        # res = []
        # n = len(nums)

        # for i in range(2 ** n):
        #     subset = []
        #     for j in range(n):
        #         if (i & 1 << j != 0):
        #             subset.append(nums[j])
        #     res.append(subset)
        # return res
        