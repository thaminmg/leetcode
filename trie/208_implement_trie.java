class Trie {
    class TrieNode {
        boolean isWord;
        Map<Character, TrieNode> children = new HashMap<>();
    }
    
    private TrieNode root;
    
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode cur = root;
        
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            
            if (cur.children.get(c) == null) {
                cur.children.put(c, new TrieNode());
            }
            
            cur = cur.children.get(c);
        }
        cur.isWord = true;
    }
    
    public boolean search(String word) {
        TrieNode cur = root;
        
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            
            if (cur.children.get(c) == null) {
                return false;
            }
            
            cur = cur.children.get(c);
        }
        return cur.isWord;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode cur = root;
        
        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            
            if (cur.children.get(c) == null) {
                return false;
            }
            
            cur = cur.children.get(c);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */