class Solution {
    
    private int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[][] res = new int[m][n];
        boolean[][] seen = new boolean[m][n];
        Queue<int[]> queue = new LinkedList<>();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    queue.offer(new int[] {i, j, 0}); 
                    seen[i][j] = true;
                }
            }          
        }
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int row = curr[0];
            int col = curr[1];
            int dist = curr[2];
            
            for (int[] direction : directions) {
                int nr = direction[0] + row;
                int nc = direction[1] + col;
                if (nr >= 0 && nc >= 0 && nr < m && nc < n && !seen[nr][nc]) {
                    seen[nr][nc] = true;
                    res[nr][nc] = dist + 1;
                    queue.offer(new int[] {nr, nc, dist + 1});
                }
            }
        }
        return res;
    }
}