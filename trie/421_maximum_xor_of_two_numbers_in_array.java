class Solution {
    
    class TrieNode {
        TrieNode[] children = new TrieNode[2];
    }

    public int findMaximumXOR(int[] nums) {

        int maxNum = nums[0];
        for (int num : nums) {
            maxNum = Math.max(maxNum, num);
        }    

        int l = (Integer.toBinaryString(maxNum)).length();
        int maxXor = 0;

        TrieNode root = new TrieNode();
        for (int num : nums) {
            TrieNode node = root, xorNode = root;
            int curXor = 0;

            for (int i = l - 1; i >= 0; i--) {
                int bit = (num >> i) & 1;
                int toggledBit = bit ^ 1;

                if (node.children[bit] == null) {
                    node.children[bit] = new TrieNode();
                }
                node = node.children[bit];

                if (xorNode.children[toggledBit] != null) {
                    curXor = curXor | (1 << i);
                    xorNode = xorNode.children[toggledBit];
                } else {
                    xorNode = xorNode.children[bit];
                }
            }
            maxXor = Math.max(maxXor, curXor);
        }
        return maxXor;
    }
}