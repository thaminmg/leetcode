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
    

    public TreeNode dfs(TreeNode node, Set<Integer> mySet, List<TreeNode> res) {
        if (node == null) {
            return null;
        }
        node.left = dfs(node.left,  mySet, res);
        node.right = dfs(node.right, mySet, res);

        if (mySet.contains(node.val)) {
            if (node.left != null) {
                res.add(node.left);
            }
            if (node.right != null) {
                res.add(node.right);
            }
            return null;
        }
        return node;
    }

    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {

        List<TreeNode> res = new ArrayList();
        Set<Integer> mySet = new HashSet();

        for (int num : to_delete) {
            mySet.add(num);
        }

        root = dfs(root, mySet, res);

        if (root != null) {
            res.add(root);
        }
        
        return res;
    }
}