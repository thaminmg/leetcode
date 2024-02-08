class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        r, c = len(mat), len(mat[0])
        q = []
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = '#'

        for row, column in q:
            for dx, dy in (1,0), (-1, 0), (0, 1), (0, -1):
                nr = row + dx
                nc = column + dy
                if 0 <= nr < r and 0 <= nc < c and mat[nr][nc] == '#':
                    mat[nr][nc] = mat[row][column] + 1
                    q.append((nr, nc))
        return mat


mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(Solution().updateMatrix(mat))