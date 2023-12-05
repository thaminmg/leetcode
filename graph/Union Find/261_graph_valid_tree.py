class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
    
        if rootX == rootY:
            return False
        self.root[rootX] = rootY
        return True
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges): return False
        uf = UnionFind(n)
        for a, b in edges:
            if not uf.union(a, b):
                return False
        return True                
        