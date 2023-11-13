import random
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

def generate_connected_components_graph(node_counts):
    graph_edges = []

    for nodes in node_counts:
        component_edges = [(i, j) for i in range(nodes) for j in range(i+1, nodes)]
        graph_edges.extend(component_edges)

    return graph_edges

def test_algorithm(generator, algorithm, configurations):
    for config in configurations:
        graph_edges = generator(config)
        print(graph_edges)
        print()
        connected_components_generator = [(range(sum(config[:i]), sum(config[:i+1]))) for i in range(len(config))]

        connected_components_algorithm = algorithm(connected_components_generator)

        print(connected_components_generator)
        print(connected_components_algorithm)

        assert (connected_components_generator) == (connected_components_algorithm), \
            f"Test failed for configuration {config}"

# Test configurations
configurations = [[10]*10, [100, 500], [250, 5, 10]]

# Run the tests
test_algorithm(generate_connected_components_graph, find_connected_components, configurations)
