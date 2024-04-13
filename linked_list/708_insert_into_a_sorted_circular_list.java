/*
// Definition for a Node.
class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
    public Node insert(Node head, int insertVal) {
        if (head == null) {
            Node cur = new Node(insertVal);
            cur.next = cur;
            return cur;
        }   
        Node cur = head;
        
        while (cur.next != head) {
            if (cur.val <= cur.next.val) {
                if (cur.val <= insertVal && insertVal <= cur.next.val) break;
            } else {
                if (cur.val <= insertVal || insertVal <= cur.next.val) break; 
            }
            cur = cur.next;
        }
        Node next = cur.next;
        cur.next = new Node(insertVal, next);

        return head;
    }
}