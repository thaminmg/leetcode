class Solution {
    char[][] _board;
    List<String> res;
    
    class TrieNode {
        String word = null;
        Map<Character, TrieNode> children = new HashMap();
    }
    
    public List<String> findWords(char[][] board, String[] words) {
        this._board = board;
        res = new ArrayList<String>();
        
        TrieNode root = new TrieNode();
        for (String word : words) {
            TrieNode node = root;
            for (char c : word.toCharArray()) {
                
                if (node.children.containsKey(c)) {
                    node = node.children.get(c);
                } else {
                    node.children.put(c, new TrieNode());
                    node = node.children.get(c);
                }
            }
            node.word = word;
        }
        
        for (int row = 0; row < board.length; row++) {
            for (int col = 0; col < board[row].length; col++) {
                if (root.children.containsKey(board[row][col])) {
                    backtrack(row, col, root);                    
                }
            }
        }
        return res;
    }
    
    public void backtrack(int row, int col, TrieNode parent) {
        
        char c = this._board[row][col];
        TrieNode curr = parent.children.get(c);
        
        if (curr.word != null) {
            res.add(curr.word);
            curr.word = null;
        }
        
        this._board[row][col] = '#';
        
        int[] rowDir = { -1, 1, 0, 0};
        int[] colDir = {0, 0, -1, 1};
        
        for (int i = 0; i < 4; i++) {
            int newRow = row + rowDir[i];
            int newCol = col + colDir[i];
            
            if (newRow < 0 || newRow >= this._board.length || newCol < 0 || newCol >= this._board[0].length) {
                continue;
            }
            if (curr.children.containsKey(this._board[newRow][newCol])) {
                backtrack(newRow, newCol, curr);            
            }
        }
        
        this._board[row][col] = c;
    }
}