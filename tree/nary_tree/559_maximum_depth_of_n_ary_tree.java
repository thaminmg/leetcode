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
    public int maxDepth(Node root) {
//         if (root == null) return 0;
//         if (root.children.isEmpty()) return 1;
//         List<Integer> heights = new ArrayList();
        
//         for (Node child : root.children) {
//             heights.add(maxDepth(child));
//         }
        
//         return Collections.max(heights) + 1;
        
        Queue<Pair<Node, Integer>> q = new LinkedList();
        q.add(new Pair(root, 1));
        int res = 0;
        
        while (!q.isEmpty()) {
            Pair<Node, Integer> p = q.poll();
            Node cur = p.getKey();
            int curDepth = p.getValue();
            
            if (cur != null) {
                res = Math.max(res, curDepth);
                for (Node child: cur.children) {
                    q.add(new Pair(child, curDepth + 1));
                }
            }
        }
        return res;
        
    }
}