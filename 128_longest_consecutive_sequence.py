class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # if not len(nums) > 0:
        #     return 0
        # hset = set(nums)
        # result = []
        # for num in nums:
        #     prev = num - 1 in hset
        #     if not prev:
        #         count = 1
        #         suff = num + 1 in hset
        #         while suff:
        #             count += 1
        #             num += 1
        #             suff = num + 1 in hset

        #         result.append(count)
        # # print(result)
        # return max(result)
        numSet = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest

print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# print(Solution().longestConsecutive([100,4,200,1,3,2]))
