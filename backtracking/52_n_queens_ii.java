class Solution {
    private Set<Integer> cols;
    private Set<Integer> posDiagonal;
    private Set<Integer> negDiagonal;
    private int res;
    private int size;
    
    public int totalNQueens(int n) {
        cols = new HashSet<>();
        posDiagonal =new HashSet<>();
        negDiagonal = new HashSet<>();
        res = 0;
        size = n;

        backtrack(0);
        return res;
    }
    
    public void backtrack(int row) {
        if (row == size) {
            res += 1;
            return;
        }
        
        for (int col = 0; col < size; col++) {
            int pos = row + col;
            int neg = row - col;
            
            if (cols.contains(col) || posDiagonal.contains(pos) || negDiagonal.contains(neg)) {
                continue;
            }
            cols.add(col);
            posDiagonal.add(pos);
            negDiagonal.add(neg);
            
            backtrack(row + 1);
            
            cols.remove(col);
            posDiagonal.remove(pos);
            negDiagonal.remove(neg);
        }
    }
}