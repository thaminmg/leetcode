/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {

    public Node dfs(Node prev, Node cur) {
        if (cur == null) return prev;

        cur.prev = prev;
        prev.next = cur;

        Node next = cur.next;
        Node tail = dfs(cur, cur.child);
        cur.child = null;
        
        return dfs(tail, next);
    }
    
    public Node flatten(Node head) {
        if (head == null) return head;
        Node res = new Node(0, null, head, null);

        dfs(res, head);
        res.next.prev = null;
        return res.next;
    }
}