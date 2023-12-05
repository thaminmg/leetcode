class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.count = n
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            self.count -= 1
        
    def getCount(self):
        return self.count
        
        
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        logs.sort()
        for log in logs:
            uf.union(log[1], log[2])
            if uf.getCount() == 1:
                return log[0]
        return -1 
        