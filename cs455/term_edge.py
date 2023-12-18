# import collections
# class Graph:
#     def __init__(self, document, d):
#         self.document = document.lower().split()
#         self.d = d
#         self.nodes = collections.defaultdict(int)
#         self.arcs = collections.defaultdict(int)
#         self.build_graph()

#     def build_graph(self):
#         for i, word in enumerate(self.document):
#             self.nodes[word] += 1
#             for j in range(i+1, min(i+self.d+1, len(self.document))):
#                 self.arcs[(word, self.document[j])] += 1

#     def get_count(self, word):
#         if word not in self.nodes:
#             raise ValueError(f"No node with name '{word}'")
#         return self.nodes[word]

#     def BFS(self, s, node_count_thresh, arc_count_thresh):
#         visited = set()
#         queue = collections.deque([s])
#         while queue:
#             node = queue.popleft()
#             if self.nodes[node] < node_count_thresh:
#                 visited.add(node)
#                 for i in range(len(self.document)):
#                     if self.document[i] == node:
#                         for j in range(i+1, min(i+self.d+1, len(self.document))):
#                             if self.arcs[(node, self.document[j])] > arc_count_thresh and self.document[j] not in visited:
#                                 queue.append(self.document[j])
#         return visited

#     def get_shortest_path(self, v):
#         # This function assumes that BFS has been run before
#         shortest_paths = {v: (None, 0)}
#         queue = collections.deque([v])
#         while queue:
#             node = queue.popleft()
#             for i in range(len(self.document)):
#                 if self.document[i] == node:
#                     for j in range(i+1, min(i+self.d+1, len(self.document))):
#                         if self.document[j] not in shortest_paths:
#                             shortest_paths[self.document[j]] = (node, shortest_paths[node][1] + 1)
#                             queue.append(self.document[j])
#         return shortest_paths

#     def find_connected_components(self, node_count_thresh, arc_count_thresh):
#         nodes = set(node for node, count in self.nodes.items() if count >= node_count_thresh)
#         arcs = {(u, v) for (u, v), count in self.arcs.items() if count > arc_count_thresh}
#         components = []
#         while nodes:
#             component = set()
#             queue = collections.deque([nodes.pop()])
#             while queue:
#                 node = queue.popleft()
#                 component.add(node)
#                 for u, v in arcs:
#                     if u == node and v in nodes:
#                         nodes.remove(v)
#                         queue.append(v)
#                     elif v == node and u in nodes:
#                         nodes.remove(u)
#                         queue.append(u)
#             components.append(component)
#         return components

class Node:
    def __init__(self, word):
        self.word = word
        self.count = 0
        self.neighbors = {}

class Graph:
    def __init__(self, d):
        self.nodes = {}
        self.distance = d

    def add_word(self, word):
        if word not in self.nodes:
            self.nodes[word] = Node(word)

    def add_edge(self, u, v):
        self.add_word(u)
        self.add_word(v)
        if v not in self.nodes[u].neighbors:
            self.nodes[u].neighbors[v] = 0
        self.nodes[u].neighbors[v] += 1

    def build_graph(self, text):
        words = text.lower().split()
        for i in range(len(words)):
            for j in range(i + 1, min(i + self.distance + 1, len(words))):
                self.add_edge(words[i], words[j])

    def get_count(self, word):
        if word not in self.nodes:
            raise ValueError(f"Node '{word}' does not exist")
        return self.nodes[word].count

    def bfs(self, s, node_count_thresh, arc_count_thresh):
        visited = set()
        queue = [s]
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                if self.get_count(current) < node_count_thresh:
                    for neighbor, count in self.nodes[current].neighbors.items():
                        if count > arc_count_thresh:
                            queue.append(neighbor)
        return visited

    def get_shortest_path(self, v):
        if not self.s:
            raise ValueError("BFS has not been run yet")
        queue = [(self.s, [])]
        visited = set()
        while queue:
            current, path = queue.pop(0)
            if current not in visited:
                visited.add(current)
                if current == v:
                    return path + [v]
                for neighbor in self.nodes[current].neighbors.keys():
                    queue.append((neighbor, path + [current]))
        return None

    def find_connected_components(self, node_count_thresh, arc_count_thresh):
        components = []
        unvisited = set(self.nodes.keys())
        while unvisited:
            current = unvisited.pop()
            visited = self.bfs(current, node_count_thresh, arc_count_thresh)
            components.append(visited)
            unvisited -= visited
        return components
    
with open("/Users/lucaszhao/Documents/Study/leetcode/cs455/term_project_doc.txt", "r") as f:
    document = f.read()

# Step 1: Find a suitable node_count_thresh
common_words = ["the", "a", "of", "and", "in", "to", "is", "for", "that", "with", "as", "on", "by", "at", "this", "it", "from", "or", "an", "be"]


# Step 2: Create two graphs and find connected components
graph_d0 = Graph(document, d=0)
counts_d0 = [graph_d0.get_count(word) for word in common_words]
node_count_thresh_d0 = min(counts_d0)  # or use average: sum(counts) / len(counts)

graph_d10 = Graph(document, d=10)
counts_d10 = [graph_d10.get_count(word) for word in common_words]
node_count_thresh_d10 = min(counts_d10)  # or use average: sum(counts) / len(counts)

# Step 3: Repeat step 2 with different thresholds

runs = [[min(counts_d0), 6], [float('inf'), 0], [max(counts_d10), 6], [0, float('inf')],[min(counts_d0) / 2, 6 / 2] ]
D = [['sport', 'rules'], ['european', 'charter'], ['swimmers', 'squats'], ['sport', 'china'], ['ancient', 'sports'], ['greeks', 'olympic']]
for run in runs:
    node_count_thresh = run[0] 
    arc_count_thresh = run[1]

    components_d0_no_thresh = graph_d0.find_connected_components(node_count_thresh, arc_count_thresh)
    components_d10_no_thresh = graph_d10.find_connected_components(node_count_thresh, arc_count_thresh)

    print(f"When node count thresh: {node_count_thresh} and arc count thresh: {arc_count_thresh},")
    print("----- D = 0 -----")
    for wi, wi_plus_1 in D:
        graph_d0.BFS(wi, node_count_thresh, arc_count_thresh)
        S = graph_d0.get_shortest_path(wi_plus_1)
        # print(wi, wi_plus_1, ' '.join(S[::-1]))
        print(wi, wi_plus_1, len(S))

    print(f"No. of connected components: {len(components_d0_no_thresh)}")
    print("========================================")
    print("----- D = 10 -----")
    for wi, wi_plus_1 in D:
        graph_d10.BFS(wi, node_count_thresh, arc_count_thresh)
        S = graph_d10.get_shortest_path(wi_plus_1)
        # print(wi, wi_plus_1, ' '.join(S[::-1]))
        print(wi, wi_plus_1, len(S))
    print(f"No. of connected components: {len(components_d10_no_thresh)}")
    print("========================================")
    print()
    print()