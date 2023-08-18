class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        degree = [0 for _ in range(n)]
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
        common = set(tuple(road) for road in roads) 
        maxRank = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = degree[i] + degree[j]
                if (i, j) in common or (j, i) in common:
                    rank -= 1
                maxRank = max(maxRank, rank)
        return maxRank

n = 4
roads = [[0,1],[0,3],[1,2],[1,3]]
print(Solution().maximalNetworkRank(n, roads))