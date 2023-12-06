class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        destination = len(graph) - 1
        
        def dfs(curr_node, stack):
            if curr_node == destination:
                res.append(stack.copy())
                return
            
            for next_node in graph[curr_node]:
                stack.append(next_node)
                dfs(next_node, stack)
                stack.pop()
        dfs(0, [0])
        return res
        