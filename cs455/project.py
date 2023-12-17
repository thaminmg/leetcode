from collections import deque

class GraphOfDocument:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, word):
        if word not in self.nodes:
            self.nodes[word] = {'count': 0}

    def add_edge(self, u, v):
        if u not in self.edges:
            self.edges[u] = {}
        if v not in self.edges[u]:
            self.edges[u][v] = {'count': 0}

    def add_occurrence(self, word):
        self.nodes[word]['count'] += 1

    def add_event_occurrence(self, u, v):
        self.edges[u][v]['count'] += 1

    def get_count(self, word):
        return self.nodes[word]['count'] if word in self.nodes else 0

    def BFS(self, s, node_count_thresh, arc_count_thresh):
        print("+++++++++ in BFS")
        visited = set()
        queue = deque([(s, None)])  # (node, parent)

        while queue:
            current, parent = queue.popleft()
            if current not in visited and self.nodes[current]['count'] < node_count_thresh:
                visited.add(current)
                yield current

                if current in self.edges:
                    for neighbor in self.edges[current]:
                        if self.edges[current][neighbor]['count'] > arc_count_thresh:
                            queue.append((neighbor, current))

    # def get_shortest_path(self, v):
    #     if v not in self.nodes:
    #         raise ValueError(f"Node {v} is unknown. Run BFS first.")

    #     path = []
    #     while v is not None:
    #         path.append(v)
    #         # v = self.edges[v]['parent']
    #         v = self.edges[v].get('parent')
    #     return list(reversed(path))
    def get_shortest_path(self, wi_plus_1):
        if wi_plus_1 not in self.edges:
            raise ValueError(f"Edge {wi_plus_1} is unknown. Run BFS first.")

        path = []
        while wi_plus_1 is not None:
            print(wi_plus_1)
            path.append(wi_plus_1)
            # v = self.edges[v]['parent']
            # print(self.edges[wi_plus_1])
            first_key = next(iter(self.edges[wi_plus_1]))
            wi_plus_1 = self.edges[wi_plus_1].get(first_key, {})
            # wi_plus_1 = self.edges[wi_plus_1][0]
        return list(reversed(path))

    def find_connected_components(self, node_count_thresh, arc_count_thresh):
        components = []
        visited = set()

        for node in self.nodes:
            if node not in visited and self.nodes[node]['count'] < node_count_thresh:
                component = list(self.BFS(node, node_count_thresh, arc_count_thresh))
                components.append(component)
                visited.update(component)

        return components

def read_document(file_path):
    with open(file_path, 'r') as file:
        return file.read().lower().split()

# Step 1
def find_node_count_thresh(document, common_words):
    counts = {word: document.count(word) for word in common_words}
    return min(counts.values())

# Step 2
def analyze_graph(d, node_count_thresh, arc_count_thresh):
    graph = GraphOfDocument()

    for i in range(len(document) - 1):
        word_u, word_v = document[i], document[i + 1]
        graph.add_node(word_u)
        graph.add_node(word_v)
        graph.add_edge(word_u, word_v)
        graph.add_occurrence(word_u)
        graph.add_event_occurrence(word_u, word_v)

    connected_components = graph.find_connected_components(node_count_thresh, arc_count_thresh)

    return [connected_components, graph]

# Step 3
def analyze_graph_variation(d, node_count_thresh, arc_count_thresh):
    graph = GraphOfDocument()

    for i in range(len(document) - 1):
        word_u, word_v = document[i], document[i + 1]
        graph.add_node(word_u)
        graph.add_node(word_v)
        graph.add_edge(word_u, word_v)
        graph.add_occurrence(word_u)
        graph.add_event_occurrence(word_u, word_v)

    connected_components = graph.find_connected_components(node_count_thresh, arc_count_thresh)

    return [connected_components, graph]

# Step 4
def analyze_dataset(graph, dataset):
    for wi, wi_plus_1 in dataset:
        graph.BFS(wi, float('inf'), 0)
        path = graph.get_shortest_path(wi_plus_1)
        print(f"{wi} {wi_plus_1} {' '.join(path)}")

# Main execution
document_file_path = "/Users/lucaszhao/Documents/Study/leetcode/cs455/term_project_doc.txt"
document = read_document(document_file_path)

common_words = ["the", "a", "of", "and", "in", "to", "is", "for", "that", "with", "as", "on", "by", "at", "this", "it", "from", "or", "an", "be"]  # Add more as needed
node_count_thresh = find_node_count_thresh(document, common_words)

# Step 2
connected_components_d0 = analyze_graph(0, node_count_thresh, 6)
connected_components_d10 = analyze_graph_variation(100, node_count_thresh, 0)

# Step 4
dataset = [["sport", "rules"], ["european", "charter"], ["swimmers", "squats"],
           ["sport", "china"], ["ancient", "sports"], ["greeks", "olympic"]]
graph_d0 = analyze_graph(0, float('inf'), 0)
analyze_dataset(graph_d0[1], dataset)
print()
print("====================")
print()
graph_d10 = analyze_graph_variation(10, float('inf'), 0)
analyze_dataset(graph_d10[1], dataset)
