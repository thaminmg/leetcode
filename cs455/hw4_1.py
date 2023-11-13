class DisjointSetCollection:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

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

def find_connected_components(graph_edges):
    n = max(max(edge) for edge in graph_edges) + 1
    print(n)
    dsc = DisjointSetCollection(n)

    for edge in graph_edges:
        dsc.union(edge[0], edge[1])

    components = {}
    for i in range(n):
        root = dsc.find(i)
        if root not in components:
            components[root] = []
        components[root].append(i)

    return list(components.values())

# Test the class and find connected components
graph_edges = [[0, 1], [2, 3], [3, 5], [4, 6]]
connected_components = find_connected_components(graph_edges)

# Output the set of nodes in each connected component
for i, component in enumerate(connected_components):
    print(f"Connected Component {i + 1}: {component}")
