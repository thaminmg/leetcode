import networkx as nx


def tokenize_text(text):
    """
    Tokenizes the text into lowercase words based on whitespace.

    Args:
        text: The text to tokenize.

    Returns:
        A list of lowercase words.
    """
    words = text.lower().split()
    return words


def build_graph(words, d):
    """
    Builds a directed graph from the list of words with distance parameter d.

    Args:
        words: The list of words.
        d: The distance parameter for connecting words.

    Returns:
        A directed graph (NetworkX object).
    """
    graph = nx.DiGraph()
    for i, word in enumerate(words):
        graph.add_node(word)
        for j in range(i + 1, min(i + d + 1, len(words))):
            graph.add_edge(word, words[j])

    return graph


def get_count(graph, word):
    """
    Returns the count of the given word in the graph.

    Args:
        graph: The graph.
        word: The word to find the count for.

    Returns:
        The count of the word in the graph.
    """
    return graph.nodes[word]["count"] if word in graph.nodes else 0


def get_shortest_path(graph, start, end):
    """
    Returns the shortest path (in terms of edges) from the start node to the end node.

    Args:
        graph: The graph.
        start: The starting node.
        end: The ending node.

    Returns:
        The shortest path from start to end (list of words).
    """
    if start not in graph.nodes:
        raise ValueError(f"Start node '{start}' not found in the graph.")
    if end not in graph.nodes:
        raise ValueError(f"End node '{end}' not found in the graph.")
    return nx.shortest_path(graph, start, end)


def find_connected_components(graph, node_count_thresh, arc_count_thresh):
    """
    Finds the connected components in the graph after suppressing nodes and arcs.

    Args:
        graph: The graph.
        node_count_thresh: The threshold for suppressing nodes (minimum count).
        arc_count_thresh: The threshold for suppressing arcs (minimum count).

    Returns:
        A list of sets of words representing the connected components.
    """
    components = []
    visited = set()
    for node in graph.nodes:
        if node in visited or get_count(graph, node) >= node_count_thresh:
            continue
        component = set()
        queue = [node]
        while queue:
            current_node = queue.pop(0)
            visited.add(current_node)
            component.add(current_node)
            for neighbor in graph.neighbors(current_node):
                if neighbor in visited or graph.edges[(current_node, neighbor)]["count"] < arc_count_thresh:
                    continue
                queue.append(neighbor)
        components.append(component)
    return components


# Read the text document
with open("/Users/lucaszhao/Documents/Study/leetcode/cs455/term_project_doc.txt", "r") as f:
    text = f.read()

# Tokenize the text
words = tokenize_text(text)

# Define the distance parameters
d1 = 0
d2 = 10

# Find a suitable node_count_thresh
excessively_common_words = ["the", "a", "of", "in"]
graph = build_graph(words, 5)
node_count_thresh = min(get_count(graph, word) for word in excessively_common_words)

# Build and analyze graphs with different settings
# Run 1: d=0, node_count_thresh
graph1 = build_graph(words, d1)
for component in find_connected_components(graph1, node_count_thresh, 6):
    print(f"Run 1, Component: {component}")
print(f"Run 1, Total Components: {len(find_connected_components(graph1, node_count_thresh, 6))}")

# Run 2: d=10, node_count_thresh
graph2 = build_graph(words, d2)
for component in find_connected_components(graph2, node_count_thresh, 6):
   print(f"Run 1, Component: {component}")
print(f"Run 1, Total Components: {len(find_connected_components(graph2, node_count_thresh, 6))}")
