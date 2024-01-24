class Solution {
    private static final int EMPTY = Integer.MAX_VALUE;
    private static final int WALL = -1;
    private static final int GATE = 0;
    private static final List<int[]> DIRECTIONS = Arrays.asList(
        new int[] {1, 0},
        new int[] {-1, 0},
        new int[] {0, 1},
        new int[] {0, -1}
    );

    public void wallsAndGates(int[][] rooms) {
        int m = rooms.length;
        int n = rooms[0].length;
        Queue<int[]> q = new LinkedList<>();
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (rooms[row][col] == GATE) {
                    q.offer(new int[] {row, col});
                }
            }
        }

        while (!q.isEmpty()) {
            int[] point = q.poll();
            int row = point[0];
            int col = point[1];

            for (int[] direction: DIRECTIONS) {
                int r = row + direction[0];
                int c = col + direction[1];
                if (r < 0 || c < 0 || r >= m || c >= n || rooms[r][c] == WALL || rooms[r][c] != EMPTY) {
                    continue;
                }
                rooms[r][c] = rooms[row][col] + 1;
                q.offer(new int[] {r, c});
            }

        }
    }

    // public void wallsAndGates(int[][] rooms) {
    //     for (int row = 0; row < rooms.length; row++) {
    //         for (int col = 0; col < rooms[0].length; col++) {
    //             if (rooms[row][col] == EMPTY) {
    //                 rooms[row][col] = distanceToNearestGate(rooms, row, col);
    //             }
    //         }
    //     }
    // }

    // private int distanceToNearestGate(int[][] rooms, int startRow, int startCol) {
    //     int m = rooms.length;
    //     int n = rooms[0].length;
    //     int[][] distance = new int[m][n];
    //     Queue<int[]> q = new LinkedList<>();
    //     q.offer(new int[] {startRow, startCol});
        
    //     while (!q.isEmpty()) {
    //         int[] point = q.poll();
    //         int row = point[0];
    //         int col = point[1];
    //         for (int[] direction: DIRECTIONS) {
    //             int r = row + direction[0];
    //             int c = col + direction[1];
    //             if (r < 0 || c < 0 || r >= m || c >= n || rooms[r][c] == WALL || distance[r][c] != 0) {
    //                 continue;
    //             }
    //             distance[r][c] = distance[row][col] + 1;
    //             if (rooms[r][c] == GATE) {
    //                 return distance[r][c];
    //             }
    //             q.offer(new int[] {r, c});
    //         }
    //     }
    //     return EMPTY;
    // }
}