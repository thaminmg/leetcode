class Solution {
    
    class TrieNode {
        List<Integer> indexList = new ArrayList<Integer>();
        Map<Character, TrieNode> children = new HashMap<>();
    }
    
    int n = 0;
    String[] words = null;
    TrieNode root = null;
        
    public List<List<String>> wordSquares(String[] words) {
        n = words[0].length();
        this.words = words;
        List<List<String>> res = new ArrayList<List<String>>();
        
        // build trie
        root = new TrieNode();
        for (int index = 0; index < words.length; index++) {
            TrieNode curr = root;
            
            for (char c : words[index].toCharArray()) {
                if (curr.children.containsKey(c)) {
                    curr = curr.children.get(c);
                } else {
                    curr.children.put(c, new TrieNode());
                    curr = curr.children.get(c);
                }
                curr.indexList.add(index);
            }
            
        }
        
        for (String word : words) {
            LinkedList<String> wordSquares = new LinkedList<>();
            wordSquares.addLast(word);
            backtrack(1, wordSquares, res);
        }
        return res;
    }
    
    public void backtrack(int step, LinkedList<String> wordSquares, List<List<String>> res) {
        if (step == n) {
            res.add((List<String>) wordSquares.clone());
            return;
        }
        
        StringBuilder prefix = new StringBuilder();
        for (String word : wordSquares) {
            prefix.append(word.charAt(step));
        }
        
        for (Integer wordIndex : getWordsWithPrefix(prefix.toString())) {
            wordSquares.addLast(this.words[wordIndex]);
            backtrack(step + 1, wordSquares, res);
            wordSquares.removeLast();
        }
    }
    
    public List<Integer> getWordsWithPrefix(String prefix) {
         TrieNode curr = root;
            
        for (char c : prefix.toCharArray()) {
            if (curr.children.containsKey(c)) {
                curr = curr.children.get(c);
            } else {
                return new ArrayList<Integer>();
            }
        }
        return curr.indexList;
    }
}