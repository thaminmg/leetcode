class TrieNode {
    Map<Character, TrieNode> children;
    Map<String, Integer> sentences;
    
    public TrieNode() {
        children = new HashMap<>();
        sentences = new HashMap<>();
    }
}

class AutocompleteSystem {
    TrieNode root, curr, dead;
    StringBuilder res;
    
    public AutocompleteSystem(String[] sentences, int[] times) {
        root = new TrieNode();
        for (int i = 0; i < sentences.length; i++) {
            addToTrie(sentences[i], times[i]);
        }
        res = new StringBuilder();
        curr = root;
        dead = new TrieNode();
    }
    
    public void addToTrie(String sentence, int time) {
        TrieNode node = root;
        for (char c : sentence.toCharArray()) {
            if (node.children.get(c) == null) {
                node.children.put(c, new TrieNode());
            }
            node = node.children.get(c);
            
            node.sentences.put(sentence, node.sentences.getOrDefault(sentence, 0) + time);
        }
        
    }
    
    public List<String> input(char c) {
        if (c == '#') {
            addToTrie(res.toString(), 1);
            res.setLength(0);
            curr = root;
            return new ArrayList<String>();
        }
        res.append(c);
        if (curr.children.get(c) == null) {
            curr = dead;
            return new ArrayList<String>();
        }
        
        curr = curr.children.get(c);
        List<String> sentences = new ArrayList<>(curr.sentences.keySet());
        Collections.sort(sentences, (a, b) -> {
            int hotA = curr.sentences.get(a);
            int hotB = curr.sentences.get(b);
            if (hotA == hotB) {
                return a.compareTo(b);
            }
            return hotB - hotA;
        });
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < Math.min(3, sentences.size()); i++) {
            ans.add(sentences.get(i));
        }
        return ans;
    }
}

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
 * List<String> param_1 = obj.input(c);
 */