class Solution {
    
    private int n = 3;
    private int size = n * n;
    private char[][] board;
    
    private int[][] rows = new int[size][size + 1];
    private int[][] cols = new int[size][size + 1];
    private int[][] boxs = new int[size][size + 1];
    
    private boolean isSolved = false;
    
    public boolean couldPlace(int d, int row, int col) {
        int idx = (row / n) * n + col / n;
        return rows[row][d] + cols[col][d] + boxs[idx][d] == 0;
    }
    public void placeNumber(int d, int row, int col) {
        int idx = (row / n) * n + col / n;
        rows[row][d]++;
        cols[col][d]++;
        boxs[idx][d]++;
        board[row][col] = (char) (d + '0');
    }
    
    public void removeNumber(int d, int row, int col) {
        int idx = (row / n) * n + col / n;
        rows[row][d]--;
        cols[col][d]--;
        boxs[idx][d]--;
        board[row][col] = '.';
    }
    
    public void placeNextNumber(int row, int col) {
        if (row == size - 1 && col == size - 1) {
            isSolved = true;
        } else if (col == size - 1) {
            backtrack(row + 1, 0);
        } else {
            backtrack(row, col + 1);
        }
    }
    
    public void backtrack(int row, int col) {
        if (board[row][col] == '.') {
            for (int d = 1; d <= size; d++) {
                if (couldPlace(d, row, col)) {
                    placeNumber(d, row, col);
                    placeNextNumber(row, col);
                    if (!isSolved) removeNumber(d, row, col);
                }
            }
        } else {
            placeNextNumber(row, col);
        }
    }
    
    public void solveSudoku(char[][] board) {
        this.board = board;
    
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (board[i][j] != '.') {
                    int d = Character.getNumericValue(board[i][j]);
                    placeNumber(d, i, j);
                }
            }
        }
        
        backtrack(0, 0);
    }
}