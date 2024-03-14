class Node {
    int val;
    Node next;
    
    public Node(int x) {
        val = x;
    }
}

class MyLinkedList {
    
    private Node head;
    
    public MyLinkedList() {
        this.head = null;
    }
    
    public int get(int index) {
        int counter = index;
        Node cur = this.head;
        
        while (counter > 0 && cur != null) {
            cur = cur.next;
            counter--;
        }
        return cur == null ? -1 : cur.val;
    }
    
    public void addAtHead(int val) {
        Node cur = new Node(val);
        cur.next = head;
        head = cur;
    }
    
    public void addAtTail(int val) {
        Node cur = new Node(val);
        if (head == null) {
            head = cur;
            return;
        }
        Node temp = this.head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = cur;
    }
    
    public void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
            return;
        }
        Node cur = new Node(val);
        Node temp = this.head;
        index--;
        while (index > 0 && temp != null) {
            temp = temp.next;
            index--;
        }
        if (temp == null) return;
        
        cur.next = temp.next;
        temp.next = cur;
    }
    
    public void deleteAtIndex(int index) {
        if (index == 0) {
            if (head != null) {
                head = head.next;
            }
            return;
        }
        Node temp = this.head;
        index--;
        while (index > 0 && temp != null) {
            temp = temp.next;
            index--;
        }
        if (temp == null || temp.next == null) return;
        temp.next = temp.next.next;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */