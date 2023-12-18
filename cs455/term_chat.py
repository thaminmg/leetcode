class TextGraph:
    def __init__(self, document, d):
        self.graph = {}
        self.node_counts = {}
        self.arc_counts = {}
        self.starting_node = None

        words = document.split()
        for i, u in enumerate(words):
            if u not in self.graph:
                self.graph[u] = set()
                self.node_counts[u] = 0

            self.node_counts[u] += 1

            if i > 0:
                v = words[i - 1]
                if v not in self.graph:
                    self.graph[v] = set()
                    self.node_counts[v] = 0

                self.graph[v].add(u)

                edge = (v, u)
                self.arc_counts[edge] = self.arc_counts.get(edge, 0) + 1

    def get_count(self, word):
        if word in self.node_counts:
            return self.node_counts[word]
        else:
            raise ValueError(f"No node with name '{word}' in the graph.")

    def BFS(self, s, node_count_thresh, arc_count_thresh):
        visited = set()
        queue = [s]
        self.starting_node = s

        while queue:
            node = queue.pop(0)

            if node not in visited and self.node_counts[node] < node_count_thresh:
                visited.add(node)

                for neighbor in self.graph[node]:
                    edge = (node, neighbor)
                    if self.arc_counts[edge] > arc_count_thresh:
                        queue.append(neighbor)

        return visited

    def get_shortest_path(self, v):
        if self.starting_node is None:
            raise ValueError("No BFS call was done before calling get_shortest_path.")

        path = []
        current = v
        while current != self.starting_node:
            path.append(current)
            neighbors = self.graph[current]
            current = min(neighbors, key=lambda neighbor: self.arc_counts[(neighbor, current)])
        path.append(self.starting_node)
        return path

    def find_connected_components(self, node_count_thresh, arc_count_thresh):
        components = []
        visited = set()

        for node in self.graph:
            if node not in visited and self.node_counts[node] < node_count_thresh:
                component = self.BFS(node, node_count_thresh, arc_count_thresh)
                visited.update(component)
                components.append(component)

        return components


# Example Usage
    
# document = "This is a sample document for text analysis. It contains words and phrases for testing the program."
node_count_thresh = 2
arc_count_thresh = 1

graph_d0 = TextGraph(document, d=0)
components_d0 = graph_d0.find_connected_components(node_count_thresh, arc_count_thresh)

graph_d10 = TextGraph(document, d=10)
components_d10 = graph_d10.find_connected_components(node_count_thresh, arc_count_thresh)

# Analyze and report differences qualitatively
print("Connected Components (d=0):", components_d0)
print("Connected Components (d=10):", components_d10)
