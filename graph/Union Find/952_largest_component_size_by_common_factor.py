class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        # self.size = [1] * (n + 1)


    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return rootX

        # if self.size[rootX] > self.size[rootY]:
        #     rootX, rootY = rootY, rootX
        self.parent[rootX] = rootY
        # self.size[rootY] += self.size[rootX]
        return rootY

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        uf = UnionFind(max(nums))

        for num in nums:
            for factor in range(2, int(sqrt(num)) + 1):
                if num % factor == 0:
                    uf.union(num, factor)
                    uf.union(num, num // factor)


        res = 0
        countHash = defaultdict(int)
        for num in nums:
            group_id = uf.find(num)
            countHash[group_id] += 1
            res = max(res, countHash[group_id])
        return res    