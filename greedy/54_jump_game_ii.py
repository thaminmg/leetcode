class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

        # not all test cases passed :'(
        # res = 0
        # n = len(nums)
        # temp = 0
        # if n == 1:
        #     return 0
        # if nums[0] >= n:
        #     return 1
        # for i in range(n - 1, 0, -1):    
        #     print(res, temp)
        #     if i - 1 >= 0 and nums[i - 1] > 0:
        #         if i != n - 1 and nums[i - 1] == temp + 1:
        #             temp = 0
        #             res += 1
        #         else:
        #             temp += 1
        #     elif i - 1 >= 0 and nums[i - 1] == 0:
        #         print('in else')
        #         temp = n - i
        #         print(temp)
            
        # return res + temp