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
class BSTIterator {

    List<Integer> sorted;
    int index;
    
    public BSTIterator(TreeNode root) {
        sorted = new ArrayList<Integer>();
        index = 0;
        
        inorder(root);
    }
    
    public void inorder(TreeNode root) {
        if (root == null) return;
        
        inorder(root.left);
        sorted.add(root.val);
        inorder(root.right);
    }
    
    public int next() {
        return sorted.get(index++);
    }
    
    public boolean hasNext() {
        return index < sorted.size();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */