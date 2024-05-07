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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        // Iteration O(H) - O(log N) to O(N) + O(1)
        if (root == null) return new TreeNode(val);
        TreeNode curr = root;
        
        while (curr.val != val) {
            if (curr.val > val) {
                if (curr.left == null) curr.left = new TreeNode(val);
                curr = curr.left;
            } else {
                if (curr.right == null) curr.right = new TreeNode(val);
                curr = curr.right;
            }
        }
        return root;
        
        // Resursion O(H) - O(log N) to O(N) + O(N)
        // if (root == null) return new TreeNode(val);
        // if (root.val > val) {
        //     root.left = insertIntoBST(root.left, val);
        // } else {
        //     root.right = insertIntoBST(root.right, val);
        // }
        // return root;
    }
}