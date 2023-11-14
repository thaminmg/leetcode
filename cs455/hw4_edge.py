class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

def find_components(edges, n):
    dsc = DisjointSet(n)
    for x, y in edges:
        dsc.union(x, y)
    components = {i: [] for i in range(n)}
    for i in range(n):
        components[dsc.find(i)].append(i)
    components = [set(nodes) for nodes in components.values() if nodes]
    return components


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


def test(node_counts):
    n = sum(node_counts)
    edges, expected_components = generate_graph(node_counts)
    print(edges)
    print()
    print(expected_components)
    print()
    found_components = find_components(edges, n)
    print(found_components)
    assert set(map(frozenset, expected_components)) == set(map(frozenset, found_components))
    print(f"Test passed for configuration {node_counts}.")

test([10]*10)
test([100,500])
test([250,5,10])
