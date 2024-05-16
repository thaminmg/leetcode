class Solution {
    class TrieNode {
        boolean isEnd;
        Map<Character, TrieNode> children = new HashMap<>();
    }
    
    private TrieNode root;
    
    public void insert(String s) {
        TrieNode cur = root;
        for (char c : s.toCharArray()) {
            TrieNode node  = cur.children.get(c);
            if (node == null) {
                cur.children.put(c, new TrieNode());
            }
            cur = cur.children.get(c);
        }
        cur.isEnd = true;
    }
    
    public String getWord(String word) {
        TrieNode cur = root;
        if (cur.children.get(word.charAt(0)) == null) return word;
        
        StringBuilder sb = new StringBuilder();
        for (char c : word.toCharArray()) {
            sb.append(c);
            TrieNode node  = cur.children.get(c);
            if (node == null) {
                return word;
            } else if (node != null && node.isEnd == true) {
                return sb.toString();
            }
            cur = node;
        }
        return sb.toString();
    }
    
    public String replaceWords(List<String> dictionary, String sentence) {
        root = new TrieNode();
        dictionary.forEach(s -> insert(s));
        
        StringBuilder sb = new StringBuilder();
        String[] words = sentence.split(" ");
        for (int i = 0; i < words.length; i++) {
            sb.append(getWord(words[i])).append(" ");
        }
        
        return sb.toString().trim();
    }
}