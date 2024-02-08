class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if r == M and c == N:
                    continue
                if r + 1 < M and c + 1 < N:
                    grid[r][c] += min(grid[r + 1][c], grid[r][c + 1])
                elif r + 1 >= M and c + 1 < N:
                    grid[r][c] += grid[r][c + 1]
                elif c + 1 >= N and r + 1 < M:
                    grid[r][c] += grid[r + 1][c]

        return grid[0][0]





grid = [[1,3,1],[1,5,1],[4,2,1]]
print(Solution().minPathSum(grid))