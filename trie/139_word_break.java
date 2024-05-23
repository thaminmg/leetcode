class Solution {
    class TrieNode {
        Map<Character, TrieNode> children = new HashMap();
        boolean isWord;
    }

    public boolean wordBreak(String s, List<String> wordDict) {
        
        // Build trie
        TrieNode root = new TrieNode();
        for (int i = 0; i < wordDict.size(); i++) {
            String word = wordDict.get(i);
            TrieNode curr = root;
            for (int j = 0; j < word.length(); j++) {
                char c = word.charAt(j);
                if (!curr.children.containsKey(c)) {
                    curr.children.put(c, new TrieNode());
                }
                curr = curr.children.get(c);
            }
            curr.isWord = true;
        }

        boolean[] dp = new boolean[s.length()];
        for (int i = 0; i < s.length(); i++) {
           if (i == 0 || dp[i - 1]) {
                TrieNode curr = root;
                for (int j = i; j < s.length(); j++) {
                    char c = s.charAt(j);
                    if (!curr.children.containsKey(c)) break;

                    curr = curr.children.get(c);
                    if (curr.isWord) {
                        dp[j] = true;
                    }
                }
           }
        }
        return dp[s.length() - 1];
    }
}