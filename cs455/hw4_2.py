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

# 2.1
def find_connected_components_algorithm(edges):
    n = max(max(edge) for edge in edges) + 1
    dsc = DisjointSetCollection(n)

    for edge in edges:
        dsc.union(edge[0], edge[1])

    components = {}
    for i in range(n):
        root = dsc.find(i)
        if root not in components:
            components[root] = []
        components[root].append(i)

    return list(components.values())

# 2.2
def generate_graph(node_counts):
    edges = []
    components = []
    start = 0
    for count in node_counts:
        component = list(range(start, start + count))
        components.append(set(component))
        for i in range(start, start + count):
            for j in range(i + 1, start + count):
                edges.append((i, j))
        start += count
    return edges, components

# 2.3
def test_generator_vs_algorithm(node_counts):
    edges, generated_components = generate_graph(node_counts)
    dsc_components = find_connected_components_algorithm(edges)
    assert set(map(frozenset, generated_components)) == set(map(frozenset, dsc_components))
    print(f"Test passed for configuration {node_counts}")

def main():
    configs = [[10]*10, [100, 500], [250, 5, 10]]

    for config in configs:  
        test_generator_vs_algorithm(config)

main()