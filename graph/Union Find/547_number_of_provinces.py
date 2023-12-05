# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size
        self.count = size

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0:
            return 0
        n = len(isConnected)
        uf = UnionFind(n)
        for row in range(n):
            for col in range(row + 1, n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)
        return uf.getCount()
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         m, n = len(isConnected), len(isConnected[0])
#         parent = [i for i in range(m)]
#         rank = [1 for _ in range(m)]
        
#         def find(x):
#             if x == parent[x]:
#                 return x
#             parent[x] = find(parent[x])
#             return parent[x]

#         def update(fromm, to):
#             for idx, val in enumerate(parent):
#                 if val == fromm:
#                     parent[idx] = to
        
#         def union(x, y):
#             rootx = find(x)
#             rooty = find(y)
#             if rootx != rooty:
#                 if rank[rootx] > rank[rooty]:
#                     parent[rooty] = rootx
#                     update(rooty, rootx)
#                 elif rank[rootx] < rank[rooty]:
#                     parent[rootx] = rooty
#                     update(rootx, rooty)
#                 else:
#                     parent[rooty] = rootx
#                     rank[rootx] += 1
#                     update(rooty, rootx)
        
#         for i in range(m):
#             for j in range(i, m):
#                 if isConnected[i][j]:
#                     union(i, j)
        
#         return len(set(parent))
                    
        
        