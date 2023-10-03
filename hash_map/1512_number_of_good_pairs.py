class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = []
        count = 0
        for num in nums:
            if num in res:
                count += res.count(num)
            res.append(num)
        return count
        