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
    public void inOrderTraversal(TreeNode root, List<Integer> inorder) {
        if (root == null) return;

        inOrderTraversal(root.left, inorder);
        inorder.add(root.val);
        inOrderTraversal(root.right, inorder);
    }

    public TreeNode createBST(List<Integer> inorder, int start, int end) {

        if (start > end) return null;

        int mid = start + (end - start) / 2;
        TreeNode leftSubtree = createBST(inorder, start, mid - 1);
        TreeNode rightSubtree = createBST(inorder, mid + 1, end);
        return new TreeNode(inorder.get(mid), leftSubtree, rightSubtree);
    }

    public TreeNode balanceBST(TreeNode root) {
        List<Integer> inorder = new ArrayList();
        inOrderTraversal(root, inorder);

        return createBST(inorder, 0, inorder.size() - 1);
    }
}