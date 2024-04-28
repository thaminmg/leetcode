/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    
    public List<Integer> preorder(Node root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) return res;
        
        Stack<Node> stack = new Stack();
        stack.push(root);
        
        while (!stack.empty()) {
            Node cur = stack.pop();
            res.add(cur.val);
            Collections.reverse(cur.children);

            for (Node child : cur.children) {
                stack.push(child);
            }
        }
        return res;
    }
}