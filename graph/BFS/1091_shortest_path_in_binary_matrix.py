class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        if grid[0][0] != 0 or grid[max_row][max_col] != 0:
            return - 1

        def get_neighbors(row, col):
            directions = [(-1,-1), (-1,0),(-1,1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]

            for row_diff, col_diff in directions:
                new_row = row + row_diff
                new_col = col + col_diff

                if not (0 <= new_row <= max_row and 0 <= new_col <= max_col) or grid[new_row][new_col]:
                    continue
                yield (new_row, new_col)

        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1

        while queue:
            row, col = queue.popleft()
            distance = grid[row][col]
            if (row, col) == (max_row, max_col):
                return distance

            for neighbor_row, neighbor_col in get_neighbors(row, col):
                grid[neighbor_row][neighbor_col] = distance + 1
                queue.append((neighbor_row, neighbor_col))
        return - 1
