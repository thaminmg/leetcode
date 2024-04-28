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
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) return res;

        Queue<Node> q = new LinkedList();
        q.offer(root);
        
        while (!q.isEmpty()) {
            List<Integer> temp = new ArrayList();
            int size = q.size();
            for (int i = 0; i < size; i++){
                Node node = q.poll();
                temp.add(node.val);
                q.addAll(node.children);
            }
            res.add(temp);
        }
        return res;
    }
}