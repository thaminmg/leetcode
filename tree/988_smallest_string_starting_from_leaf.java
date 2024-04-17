/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    String res = "";
    public String smallestFromLeaf(TreeNode root) {
        dfs(root, "");
        return res;
    }

    public void dfs(TreeNode root, String currString) {
        if (root == null) return;

        currString = (char) (root.val + 'a') + currString;

        if (root.left == null && root.right == null) {
            if (res.isEmpty() || res.compareTo(currString) > 0) {
                res = currString;
            }
        }

        if (root.left != null) dfs(root.left, currString);
        if (root.right != null) dfs(root.right, currString);
    }
}