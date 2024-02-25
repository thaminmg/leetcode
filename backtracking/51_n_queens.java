class Solution {
    private Set<Integer> cols;
    private Set<Integer> posDiagonal;
    private Set<Integer> negDiagonal;
    private List<List<String>> res;
    private int size;
    private char[][] board; 
    public List<List<String>> solveNQueens(int n) {
        size = n;   
        board = new char[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                board[i][j] = '.';
            }
        }
        cols = new HashSet<>();
        posDiagonal =new HashSet<>();
        negDiagonal = new HashSet<>();
        res = new ArrayList<List<String>>();

        backtrack(0);
        return res;
    }

    public List<String> createBoard(char[][] board) {
        List<String> res = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            String rowStr = new String(board[i]);
            res.add(rowStr);
        }
        return res;
    }

    public void backtrack(int row) {
        if (row == size) {
            res.add(createBoard(board));
            return;
        }

        for (int col = 0; col < size; col++) {
            int pos = row  + col;
            int neg = row - col;
            if (cols.contains(col) || posDiagonal.contains(pos) || negDiagonal.contains(neg)) {
                continue;
            }
            cols.add(col);
            posDiagonal.add(pos);
            negDiagonal.add(neg);
            board[row][col] = 'Q';

            backtrack(row + 1);

            cols.remove(col);
            posDiagonal.remove(pos);
            negDiagonal.remove(neg);
            board[row][col] = '.';
        }
    }
}