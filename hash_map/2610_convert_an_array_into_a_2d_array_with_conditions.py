class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        hset = defaultdict(int)

        for num in nums:
            hset[num] += 1

        maxx = max(hset.values())

        for i in range(maxx):
            temp = []
            for k, v in hset.items():
                if v != 0:
                    hset[k] -= 1
                    temp.append(k)
            res.append(temp)
        return res