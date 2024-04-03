class Solution {
    char[][] board;
    int ROWS;
    int COLS;
    String word;
    // O(N . 3^L) + O(L)
    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.ROWS = board.length;
        this.COLS = board[0].length;
        this.word = word;

        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (backtrack(i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean backtrack(int row, int col, int index) {
        if (index >= word.length()) return true;

        if (row < 0 || row >= ROWS || col < 0 || col >= COLS || word.charAt(index) != board[row][col]) {
            return false;
        }

        boolean res = false;
        board[row][col] = '#';

        int[] rowOffset = {1, 0, -1, 0};
        int[] colOffset = {0, -1, 0, 1};
        for (int d = 0; d < 4; d++) {
            res = backtrack(row + rowOffset[d], col + colOffset[d], index + 1);
            if (res) {
                break;
            }
        }
        board[row][col] = word.charAt(index);
        return res;
    }
}