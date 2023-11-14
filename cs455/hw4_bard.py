class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.size[x_root] < self.size[y_root]:
            x_root, y_root = y_root, x_root

        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]

def find_connected_components(graph):
    n = len(graph)
    ds = DisjointSet(n)

    for u in range(n):
        for v in range(n):
            if graph[u][v] == 1:
                ds.union(u, v)

    components = {}
    for i in range(n):
        root = ds.find(i)
        components.setdefault(root, []).append(i)

    return components

def generate_graph(components_sizes):
    n = sum(components_sizes)
    graph = [[0 for _ in range(n)] for _ in range(n)]
    print(graph)
    component_index = 0
    for component_size in components_sizes:
        for i in range(component_index, component_index + component_size):
            for j in range(component_index, component_index + component_size):
                graph[i][j] = 1
                graph[j][i] = 1

        component_index += component_size

    return graph, components_sizes

def test_connected_components():
    configurations = [[10] * 10, [100, 500], [250, 5, 10]]

    for config in configurations:
        graph, component_sizes = generate_graph(config)
        components = find_connected_components(graph)

        for i, component in enumerate(components.values()):
            assert len(component) == component_sizes[i]
            for node in component:
                assert all(graph[node][j] == 1 for j in component)
                assert all(graph[j][node] == 1 for j in component)
        break
        print(f"Test passed for configuration {config}.")

test_connected_components()
