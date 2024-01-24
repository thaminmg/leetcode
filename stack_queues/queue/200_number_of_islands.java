class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int numberOfIslands = 0;
        int[][] DIRECTIONS = {{1,0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (grid[row][col] == '1') {
                    numberOfIslands++;
                    grid[row][col] = '0';
                    Queue<int[]> q = new LinkedList<>();
                    q.offer(new int[] {row, col});

                    while (!q.isEmpty()) {
                        int[] point = q.poll();
                        int qr = point[0];
                        int qc = point[1];
                        for (int[] direction: DIRECTIONS) {
                            int r = qr + direction[0];
                            int c = qc + direction[1];
                            if (r < 0 || c < 0 || r >= m || c >= n || grid[r][c] == '0') {
                                continue;
                            }
                            grid[r][c] = '0';
                            q.offer(new int[] {r, c});
                        }
                    }           
                }      
            }
        }
        return numberOfIslands;   
    }
}