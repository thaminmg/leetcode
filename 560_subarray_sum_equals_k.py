class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        curSum = 0
        res = 0
        prefixSum = {0 : 1}
        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSum.get(diff, 0)
            if curSum in prefixSum:
                prefixSum[curSum] += 1
            else:
                prefixSum[curSum] = 1

            # # else:
            # #     prefixSum[curSum] = 1
            # print(f'curSum {curSum} diff {diff} res {res} prefixSum {prefixSum}')a
            
        return res

print(Solution().subarraySum([1,-1,1,1,1,1], 3))
# print(Solution().subarraySum([1,1,-1,1], 1))

