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
    public int sumNumbers(TreeNode root) {
        return preorder(root, 0);
    }

    public int preorder(TreeNode root, int val) {
        if (root == null) return 0;
        int sum = val * 10 + root.val;

        if (root.left == null && root.right == null) {
            return sum;
        }
        return preorder(root.left, sum) + preorder(root.right, sum);
    }
    
    // public int sumNumbers(TreeNode root) {
    //     int res = 0, cur = 0;
    //     ArrayDeque<Pair<TreeNode, Integer>> stack = new ArrayDeque();
    //     stack.push(new Pair(root, 0));

    //     while (!stack.isEmpty()) {
    //         Pair<TreeNode, Integer> p = stack.pop();
    //         root = p.getKey();
    //         cur = p.getValue();

    //         if (root != null) {
    //             cur = cur * 10 + root.val;
    //             if (root.left == null && root.right == null) {
    //                 res += cur;
    //             } else {
    //                 stack.push(new Pair(root.right, cur));
    //                 stack.push(new Pair(root.left, cur));
    //             }
    //         }
    //     }
    //     return res;
    // }
}