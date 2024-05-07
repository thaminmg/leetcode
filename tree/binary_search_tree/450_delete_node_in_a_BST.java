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
    
    public TreeNode inOrderSuccessor(TreeNode root) {
        TreeNode curr = root.right;
        while (curr != null && curr.left != null) {
            curr = curr.left;
        }
        return curr;
    }
    
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return root;
        
        if (root.val == key) {
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            
            TreeNode succ = inOrderSuccessor(root);
            root.val = succ.val;
            root.right = deleteNode(root.right, succ.val);
            return root;
        }
        
        if (root.val > key) {
            root.left = deleteNode(root.left, key);
        } else {
            root.right = deleteNode(root.right, key);
        }
        
        return root;
    }
}