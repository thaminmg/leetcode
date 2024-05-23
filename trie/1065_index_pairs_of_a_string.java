class Solution {
    class TrieNode {
        boolean isWord;
        Map<Character, TrieNode> children = new HashMap();
    }

    public int[][] indexPairs(String text, String[] words) {
        TrieNode root = new TrieNode();
        for (String word : words) {
            TrieNode curr = root;

            for (int i = 0; i < word.length(); i++) {
                char c = word.charAt(i);

                if (!curr.children.containsKey(c)) {
                    curr.children.put(c, new TrieNode());
                }
                curr = curr.children.get(c);
            }
            curr.isWord = true;
        }

        List<int[]> res = new ArrayList();
        for (int i = 0; i < text.length(); i++) {
            TrieNode curr = root;
            for (int j = i; j < text.length(); j++) {
                char c = text.charAt(j);
                if (!curr.children.containsKey(c)) break;
                curr = curr.children.get(c);
                if (curr.isWord) {
                    res.add(new int[] {i, j});
                }
            }
        }

        int[][] ans = new int[res.size()][];
        ans = res.toArray(ans);
        return ans;  
    }
}