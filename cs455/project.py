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

# from collections import defaultdict, deque
# from queue import Queue
# import string

# class Graph:
#     def __init__(self, document, d):
#         self.document = self.clean_words(document)
#         self.d = d
#         self.graph = defaultdict(list)
#         self.counts = defaultdict(int)
#         self.arc_counts = defaultdict(int)
#         self.build_graph()
#         self.current_bfs = []

#     def clean_words(self, words):
#         punctuations = set(string.punctuation) # - set(['.'])
#         numbers = set(string.digits)
#         words = []
#         raw = document.lower().split()
#         for text in raw:
#             words.append("".join(char for char in text if char not in (punctuations | numbers)))
#         return words

#     def build_graph(self):
#         for i, word in enumerate(self.document):
#             self.counts[word] += 1
#             for j in range(i+1, min(i+self.d+1, len(self.document))):
#                 if word != self.document[j]:
#                     # distinct node ? 
#                     # if self.document[j] not in self.graph[word]:
#                     self.graph[word].append(self.document[j])
#                     self.arc_counts[(word, self.document[j])] += 1

#     def get_count(self, word):
#         if word not in self.counts:
#             raise ValueError(f"No node with name {word}")
#         return self.counts[word]

#     def BFS(self, s, node_count_thresh, arc_count_thresh):
        
#         visited = set()
#         queue = [(s, 0)]
#         start_node = s
#         distances = {}
#         while queue:
#             node, distance = queue.pop(0)
#             if node not in visited and self.counts[node] < node_count_thresh:
#                 visited.add(node)
#                 distances[node] = distance
#                 for neighbor in self.graph[node]:
#                     if self.arc_counts[(node, neighbor)] > arc_count_thresh and neighbor not in visited:
#                         queue.append((neighbor, distance + 1))
#         # print()
#         # print("--- visited ---", start_node, " --> ", visited)
#         return start_node, visited, distances
                        
#     def get_shortest_path(self, start_node, v, visited, distances):  
#         if start_node is None:
#             raise ValueError("BFS not performed before calling get_shortest_path")
#         if v not in visited:
#             return ["Node {} is not reachable from {}".format(v, start_node)]
#         print(visited)
#         # print(distances)
#         path = []
#         current_node = v
#         while current_node != start_node:
#             print('in while')
#             path.insert(0, current_node)
#             current_node = self.predecessor(current_node, visited, distances)
#             if current_node is None:
#                 break  # Break the loop if no predecessor is found

#         return [start_node] + path
#         # visited = set()
#         # queue = [(start_node, [])]  # (node, path from start_node)
#         # queue = deque()
#         # path = [start_node]
#         # queue.append(path)
#         # queue = [(start_node, [])]  # (node, path from start_node)

#         # while queue:
#         #     current_node, path = queue.pop(0)

#         #     if current_node == v:
#         #         return path + [v]  # Return the shortest path

#         #     # Enqueue neighbors that are visited in BFS
#         #     for neighbor in self.graph[current_node]:
#         #         if neighbor in visited:
#         #             queue.append((neighbor, path + [current_node]))

#         # return ["No path found from {} to {}".format(start_node, v)]
    
#     def predecessor(self, node, visited, distances):
#         for neighbor in self.graph[node]:
#             if neighbor in visited and distances[neighbor] == distances[node] - 1:
#                 return neighbor
#         return None
#     def find_connected_components(self, node_count_thresh, arc_count_thresh):
#         components = []
#         visited = set() 

#         for node in self.graph.keys():
#             if self.counts[node] < node_count_thresh or node in visited:
#                 continue

#             component = set()
#             queue = [node]

#             while queue:
#                 current_node = queue.pop(0)

#                 if current_node not in visited:
#                     visited.add(current_node)
#                     component.add(current_node)

#                     # Process neighbors without considering arc counts
#                     queue.extend(self.graph[node])

#             components.append(component)

#         return components
    
   
# with open("/Users/lucaszhao/Documents/Study/leetcode/cs455/term_project_doc.txt", "r") as f:
#     document = f.read()

# # Step 1: Find a suitable node_count_thresh
# common_words = ["the", "a", "of", "and", "in", "to", "is", "for", "that", "with", "as", "on", "by", "at", "this", "it", "from", "or", "an", "be", ""]


# # Step 2: Create two graphs and find connected components
# graph_d0 = Graph(document, d=0)
# counts_d0 = [graph_d0.get_count(word) for word in common_words]
# node_count_thresh_d0 = min(counts_d0)  # or use average: sum(counts) / len(counts)

# graph_d10 = Graph(document, d=10)
# counts_d10 = [graph_d10.get_count(word) for word in common_words]
# node_count_thresh_d10 = min(counts_d10)  # or use average: sum(counts) / len(counts)

# # Step 3: Repeat step 2 with different thresholds

# runs = [[min(counts_d0), 6], [float('inf'), 0]]#,  [0, float('inf')],[min(counts_d0) / 2, 6 / 2] ] #[max(counts_d10), 6],
# D = [['sport', 'rules'], ['european', 'charter'], ['swimmers', 'squats'], ['sport', 'china'], ['ancient', 'sports'], ['greeks', 'olympic']]
# for run in runs:
#     node_count_thresh = run[0] 
#     arc_count_thresh = run[1]

#     components_d0_no_thresh = graph_d0.find_connected_components(node_count_thresh, arc_count_thresh)
#     components_d10_no_thresh = graph_d10.find_connected_components(node_count_thresh, arc_count_thresh)

#     print(f"When node count thresh: {node_count_thresh} and arc count thresh: {arc_count_thresh},")
#     print("----- D = 0 -----")
#     for wi, wi_plus_1 in D:
#         start_node, visited, distances = graph_d0.BFS(wi, node_count_thresh, arc_count_thresh)
#         S = graph_d0.get_shortest_path(start_node, wi_plus_1, visited, distances)
#         print(wi, wi_plus_1, ': ', ' '.join(S[::-1]))
#     print(f"No. of connected components: {len(components_d0_no_thresh)}")
#     print("========================================")
#     print("----- D = 10 -----")
#     for wi, wi_plus_1 in D:
#         start_node, visited, distances = graph_d10.BFS(wi, node_count_thresh, arc_count_thresh)
#         S = graph_d10.get_shortest_path(start_node, wi_plus_1, visited, distances)
#         print(wi, wi_plus_1, ': ', ' '.join(S[::-1]))
#     print(f"No. of connected components: {len(components_d10_no_thresh)}")
#     print("========================================")
#     print()
#     print()



#     # def BFS(self, s, node_count_thresh, arc_count_thresh):
#     #     # BFS run should also explicitly record what the starting node was so that subsequent operations can leverage this
#     #     visited = set()
#     #     queue = Queue()
#     #     queue.put(s)
#     #     while not queue.empty():
#     #         node = queue.get()
#     #         if self.counts[node] < node_count_thresh:
#     #             visited.add(node)
#     #             for neighbor in self.graph[node]:
#     #                 if self.arc_counts[(node, neighbor)] > arc_count_thresh and neighbor not in visited:
#     #                     queue.put(neighbor)
#     #     return visited
#     #     # return list(visited)
                        

#     # def get_shortest_path(self, v):
#     #     parent = {v: None}
#     #     queue = Queue()
#     #     queue.put(v)
#     #     while not queue.empty():
#     #         node = queue.get()
#     #         for neighbor in self.graph[node]:
#     #             if neighbor not in parent:
#     #                 parent[neighbor] = node
#     #                 queue.put(neighbor)
#     #     path = []
#     #     while v is not None:
#     #         path.append(v)
#     #         v = parent[v]
#     #     return path[::-1]
    
#     # def main():

#     # for wi, wi_plus_1 in D:
#     #     graph_d0.BFS(wi, node_count_thresh, arc_count_thresh)
#     #     S = graph_d0.get_shortest_path(wi_plus_1)
#     #     print(wi, wi_plus_1, ' '.join(S[::-1]))


#     # sunday  
#     # BFS run should also explicitly record what the starting node was so that subsequent operations can leverage this
#         # visited = set()
#         # queue = Queue()
#         # queue.put(s)
#         # while not queue.empty():
#         #     node = queue.get()
#         #     if self.counts[node] < node_count_thresh:
#         #         visited.add(node)
#         #         for neighbor in self.graph[node]:
#         #             if self.arc_counts[(node, neighbor)] > arc_count_thresh and neighbor not in visited:
#         #                 queue.put(neighbor)
#         # return visited
#     # def get_shortest_path(self, v):
#     #     parent = {v: None}
#     #     queue = Queue()
#     #     queue.put(v)
#     #     while not queue.empty():
#     #         node = queue.get()
#     #         for neighbor in self.graph[node]:
#     #             if neighbor not in parent:
#     #                 parent[neighbor] = node
#     #                 queue.put(neighbor)
#     #     path = []
#     #     while v is not None:
#     #         path.append(v)
#     #         v = parent[v]
#     #     return path[::-1]


#     # def find_connected_components(self, node_count_thresh, arc_count_thresh):
#     #     visited = set()
#     #     components = []
#     #     for node in self.counts:
#     #         if node not in visited and self.counts[node] < node_count_thresh:
#     #             component = self.BFS(node, node_count_thresh, arc_count_thresh)
#     #             visited.update(component)
#     #             # visited.extend(component)
#     #             components.append(component)
#     #     return components


# # def get_shortest_path(self, start_node, v, visited):  
# #         if start_node is None:
# #             raise ValueError("BFS not performed before calling get_shortest_path")
# #         if v not in visited:
# #             return ["Node {} is not reachable from {}".format(v, start_node)]
# #         # visited = set()
# #         # queue = [(start_node, [])]  # (node, path from start_node)
# #         queue = deque()
# #         path = [start_node]
# #         queue.append(path)
# #         while queue:
# #             # node, path = queue.pop(0)
# #             current_path = queue.popleft()
# #             node = current_path[-1]
# #             for neighbor in self.graph[node]:
# #                 temp_path = current_path.copy()
# #                 temp_path.append(neighbor)

# #                 if neighbor == v:
# #                     return temp_path  # Return the shortest path

# #                 if neighbor not in visited:
# #                     visited.add(node)
# #                     queue.append(temp_path)

# #         # If no path is found
# #         # raise ValueError("No path found from {} to {}".format(start_node, v))
# #         return ["No path found from {} to {}".format(start_node, v)]
    

   