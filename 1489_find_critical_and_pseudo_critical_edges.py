class UnionFind:
    def __init__(self, n) -> None:
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v1):
        while v1 != self.par[v1]:
            self.par[v1] = self.par[self.par[v1]]
            v1 = self.par[v1]
        return v1
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        for i, e in enumerate(edges):
            e.append(i)

        edges.sort(key = lambda e: e[2])

        mst_weight = 0
        uf = UnionFind(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w
            
        critical, pseudo = [], []
        for n1, n2, e_weight, i in edges:
            weight = 0
            uf = UnionFind(n)
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue

            uf = UnionFind(n)
            uf.union(n1, n2)
            weight = e_weight

            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)
        return [critical, pseudo]

n = 5
edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]

print(Solution().findCriticalAndPseudoCriticalEdges(n, edges))