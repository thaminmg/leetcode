class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        fresh = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        queue.append((-1, -1))

        res = -1
        dirs = [(-1,0), (0,1), (1, 0), (0, -1)]

        while queue:
            row, col = queue.popleft()
            if row == -1:
                res += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for d in dirs:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                        if grid[neighbor_row][neighbor_col] == 1:
                            grid[neighbor_row][neighbor_col] = 2
                            fresh -= 1
                            queue.append((neighbor_row, neighbor_col))

        return res if fresh == 0 else -1
        
        