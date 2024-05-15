class MapSum {
    class NodeTrie {
        int val;
        Map<Character, NodeTrie> children = new HashMap<>();        
    }
    
    private NodeTrie root;
    private Map<String, Integer> map;
    
    public MapSum() {
        root = new NodeTrie();
        map = new HashMap<>();
    }
    
    public void insert(String key, int val) {
        int diff = val - map.getOrDefault(key, 0);
        map.put(key, val);
        NodeTrie cur = root;
        cur.val = diff;
        
        for (int i = 0; i < key.length(); i++) {
            char c = key.charAt(i);
            
            if (cur.children.get(c) == null) {
                cur.children.put(c, new NodeTrie());
            }
            cur.children.get(c).val += diff;
            cur = cur.children.get(c);
        }
    }
    
    public int sum(String prefix) {
        NodeTrie cur = root;
        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            if (cur.children.get(c) == null) {
                return 0;
            }
            cur = cur.children.get(c);
        }
        return cur.val;
    }
    
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */