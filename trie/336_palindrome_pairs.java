class TrieNode {
    Map<Character, TrieNode> children = new HashMap();        
    List<Integer> prefixPalindromes = new ArrayList();
    int ending = -1;
}

class Solution {
    public boolean hasPalindrome(String s, int i) {
        int p1 = i, p2 = s.length() - 1;
        while (p1 < p2) {
            if (s.charAt(p1) != s.charAt(p2)) {
                return false;
            }
            p1++;
            p2--;
        }
        return true;
    }
    public List<List<Integer>> palindromePairs(String[] words) {
        TrieNode root = new TrieNode();

        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            String reversedWord = new StringBuilder(word).reverse().toString();
            TrieNode curr = root;
            for (int j = 0; j < word.length(); j++) {
                if (hasPalindrome(reversedWord, j)) {
                    curr.prefixPalindromes.add(i);
                }

                char c = reversedWord.charAt(j);
                if (!curr.children.containsKey(c)) {
                    curr.children.put(c, new TrieNode());
                }
                curr = curr.children.get(c);
            }
            curr.ending = i;
        }

        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            TrieNode curr = root;
            for (int j = 0; j < word.length(); j++) {
                if (curr.ending != -1 && hasPalindrome(word, j)) {
                    res.add(Arrays.asList(i, curr.ending));
                }
                char c = word.charAt(j);
                curr = curr.children.get(c);
                if (curr == null) break;
            }
            if (curr == null) continue;

            if (curr.ending != -1 && curr.ending != i) {
                res.add(Arrays.asList(i, curr.ending));
            }

            for (int other : curr.prefixPalindromes) {
                res.add(Arrays.asList(i, other));
            }
        }
        return res;
    }
}