/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    Map<Node, Node> hashMap = new HashMap<>();
    
    public Node copyRandomList(Node head) {
        if (head == null) return head;
        if (hashMap.containsKey(head)) return hashMap.get(head);
        
        Node temp = new Node(head.val, null, null);
        hashMap.put(head, temp);
        
        temp.next = this.copyRandomList(head.next);
        temp.random = this.copyRandomList(head.random);
        return temp;
    }
}