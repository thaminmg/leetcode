class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for origin, dest in edges:
            graph[origin].append(dest)
        states = [None] * n # whether the node already created loops or not, True = no loop, False = loops

        def dfs(node):
            if states[node] != None: return states[node]
            if not graph[node]: return node == destination
            states[node] = False #temp mark as False 
            for next_node in graph[node]:
                if not dfs(next_node): return False
            states[node] = True
            return True
      
        return dfs(source)
        