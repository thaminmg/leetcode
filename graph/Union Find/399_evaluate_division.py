class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        def find(node_id):
            if node_id not in graph:
                graph[node_id] = (node_id, 1)
            group_id, node_weight = graph[node_id]

            if group_id != node_id:
                new_group_id, group_weight = find(group_id)
                graph[node_id] = (new_group_id, node_weight * group_weight)
            return graph[node_id]

        def union(dividend, divisor, value):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                graph[dividend_gid] = (divisor_gid, divisor_weight * value / dividend_weight)


        res = []
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                res.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    res.append(-1.0)
                else:
                    res.append(dividend_weight / divisor_weight)
        return res