class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        source = 0
        destination = len(graph) - 1
                 
        queue = deque()
        path = [source]
        queue.append(path)
    
        res = []
        while queue:
            current_path = queue.popleft()
            node = current_path[-1]                     
            for neighbor in graph[node]:
                temp_path = current_path.copy()
                temp_path.append(neighbor)
                if neighbor == len(graph) - 1:
                    res.append(temp_path)
                else:
                    queue.append(temp_path)
                
        return res