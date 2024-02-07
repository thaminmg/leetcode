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
    
    List<TreeNode> res = new ArrayList();
    
    public List<TreeNode> generate(int left, int right) {
        if (left == right) {
            return Arrays.asList(new TreeNode(left));
        } 
        if (left > right) {
            return Collections.singletonList(null);
        }
        
        List<TreeNode> res = new ArrayList();
        
        for (int val = left; val < right + 1; val++) {
            List<TreeNode> leftTree = generate(left, val - 1);
            
            for (TreeNode leftT : leftTree) {
                List<TreeNode> rightTree = generate(val + 1, right);

                for (TreeNode rightT: rightTree) {
                    TreeNode root = new TreeNode(val, leftT, rightT);
                    res.add(root);
                }
            }
            
        }
        return res;
        
    }
    
    public List<TreeNode> generateTrees(int n) {
        return generate(1, n);
    }
}