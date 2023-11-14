class DisjointSetCollection:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def main():
    graph_edges = [[0, 1], [2, 3], [3, 5], [4, 6]]
    n = max(max(edge) for edge in graph_edges) + 1
    dsc = DisjointSetCollection(n)

    for edge in graph_edges:
        dsc.union(edge[0], edge[1])

    components = {}
    for i in range(n):
        root = dsc.find(i)
        if root not in components:
            components[root] = []
        components[root].append(i)

    for i, component in enumerate(list(components.values())):
        print(f"Connected Component {i + 1}: {component}")

main()