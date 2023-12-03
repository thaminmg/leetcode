class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] == self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                self.update(rootY, rootX)
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
                self.update(rootX, rootY)
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
                self.update(rootY, rootX)

    def update(self, fromm, to):
        for idx, val in enumerate(self.root):
            if val == fromm:
                self.root[idx] = to
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        return len(set(uf.root))
        