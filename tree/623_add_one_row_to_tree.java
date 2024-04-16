// /**
//  * Definition for a binary tree node.
//  * public class TreeNode {
//  *     int val;
//  *     TreeNode left;
//  *     TreeNode right;
//  *     TreeNode() {}
//  *     TreeNode(int val) { this.val = val; }
//  *     TreeNode(int val, TreeNode left, TreeNode right) {
//  *         this.val = val;
//  *         this.left = left;
//  *         this.right = right;
//  *     }
//  * }
//  */
class Solution {

    public void dfs(TreeNode node, int val, int depth, int n) {
        if (node == null) return;
        
        if (n == depth - 1) {
            TreeNode cur = node.left;
            node.left = new TreeNode(val);
            node.left.left = cur;
            cur = node.right;
            node.right = new TreeNode(val);
            node.right.right = cur;
        } else {
            dfs(node.left, val, depth, n + 1);
            dfs(node.right, val, depth, n + 1);
        }
    }

    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) {
            TreeNode temp = new TreeNode(val);
            temp.left = root;
            return temp;
        }
        dfs(root, val, depth, 1);
        return root;
    }
}
        