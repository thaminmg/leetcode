class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        hset = defaultdict(int)
        for num in nums:
            hset[num] += 1

        for item in hset.values():
            if item == 1:
                return -1
            res += ceil(item / 3)
        
        return res
        