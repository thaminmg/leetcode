from collections import defaultdict, deque
from queue import Queue
import string

class Graph:
    def __init__(self, document, d):
        self.document = self.clean_words(document)
        self.d = d
        self.graph = defaultdict(list)
        self.counts = defaultdict(int)
        self.arc_counts = defaultdict(int)
        self.bsf_start = None
        self.dist = {}
        self.visited = set()
        self.build_graph()

    def clean_words(self, words):
        punctuations = set(string.punctuation)
        numbers = set(string.digits)
        words = []
        raw = document.lower().split()
        for text in raw:
            words.append("".join(char for char in text if char not in (punctuations | numbers)))
        return words

    def build_graph(self):
        for i, word in enumerate(self.document):
            self.counts[word] += 1
            for j in range(i+1, min(i+self.d+1, len(self.document))):
                if word != self.document[j]:
                    if self.document[j] not in self.graph[word]:
                        self.graph[word].append(self.document[j])
                    self.arc_counts[(word, self.document[j])] += 1

    def get_count(self, word):
        if word not in self.counts:
            raise ValueError(f"No node with name {word}")
        return self.counts[word]

    def BFS(self, s, node_count_thresh, arc_count_thresh):
        self.bfs_start = s
        self.dist = {s: 0}
        visited = set()
        q = Queue()
        q.put(s)

        while not q.empty():
            node = q.get()
            if self.counts[node] < node_count_thresh:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if self.arc_counts[(node, neighbor)] > arc_count_thresh and neighbor not in visited:
                        q.put(neighbor)
                        self.dist[neighbor] = self.dist[node] + 1
        self.visited = visited
        return self.visited

    def get_shortest_path(self, v):
        if self.bfs_start is None:
            raise ValueError("BFS must be run before calling get_shortest_path")
        
        if v not in self.visited:
            return ["No path found"]
        
        path = [v]
        while v != self.bfs_start:
            for node in self.graph:
                if self.dist.get(node) == self.dist.get(v) - 1 and v in self.graph[node]:
                    path.append(node)
                    v = node
                    break
        return path[::-1]

    def find_connected_components(self, node_count_thresh, arc_count_thresh):
        visited = set()
        components = []
        for node in self.counts:
            if node not in visited and self.counts[node] < node_count_thresh:
                self.visited.clear()
                component = self.BFS(node, node_count_thresh, arc_count_thresh)
                visited.update(component)
                components.append(component)
        return components
       
   
with open("./term_project_doc.txt", "r") as f:
    document = f.read()

# Step 1
common_words = ["the", "a", "of", "and", "in", "to", "is", "for", "that", "with", "as", "on", "by", "at", "this", "it", "from", "or",
                 "an", "be", ""]

graph_d0 = Graph(document, d=0)
counts_d0 = [graph_d0.get_count(word) for word in common_words]

graph_d10 = Graph(document, d=10)
counts_d10 = [graph_d10.get_count(word) for word in common_words]

for i in range(4):
    print(f"run no. = {i+1}")
    print()
    # Step 2
    components_d0_thresh = graph_d0.find_connected_components(min(counts_d0), 6)
    components_d10_thresh = graph_d10.find_connected_components(min(counts_d10), 6)
    # Step 3
    components_d0_no_thresh = graph_d0.find_connected_components(float('inf'), 0)
    components_d10_no_thresh = graph_d10.find_connected_components(float('inf'), 0)
    print(f"No. of connected components (d = 0, node_thresh = min(node_thresh) , arc_thresh = 6): {len(components_d0_thresh)}")
    print(f"No. of connected components (d = 10, node_thresh = min(node_thresh) , arc_thresh = 6): {len(components_d10_thresh)}")
    print(f"No. of connected components (d = 0, node_thresh = inf , arc_thresh = 0): {len(components_d0_no_thresh)}")
    print(f"No. of connected components (d = 10, node_thresh = inf , arc_thresh = 0): {len(components_d10_no_thresh)}")
    print()

# Step 4
D = [['sport', 'rules'], ['european', 'charter'], ['swimmers', 'squats'], ['sport', 'china'], ['ancient', 'sports'], ['greeks', 'olympic']]
print()
print("When d = 0:")
print()
for wi, wi_plus_1 in D:
    graph_d0.BFS(wi, float('inf'), 0)
    S = graph_d0.get_shortest_path(wi_plus_1)
    print(wi, wi_plus_1, ': ', ' '.join(S[::-1]))
print()
print("When d = 10:")
print()
for wi, wi_plus_1 in D:
    graph_d10.BFS(wi, float('inf'),  0)
    S = graph_d10.get_shortest_path(wi_plus_1)
    print(wi, wi_plus_1, ': ', ' '.join(S[::-1]))
