class DoublyListNode {
    int val;
    DoublyListNode prev, next;
    
    DoublyListNode(int x) {
        val = x;
    };
    
}

class MyLinkedList {
    
    DoublyListNode head;
    public MyLinkedList() {
        this.head = null;
    }
    
    public DoublyListNode getNode(int index) {
        DoublyListNode temp = head;
        
        while (--index >= 0 && temp != null) {
            temp = temp.next;
        }
        return temp;
    }
    
    public DoublyListNode getTail() {
        DoublyListNode temp = head;
        while (temp != null && temp.next != null) {
            temp = temp.next;
        }
        return temp;
    }
    
    public int get(int index) {
        DoublyListNode cur = getNode(index);
        return cur == null ? - 1 : cur.val;
    }
    
    public void addAtHead(int val) {
        DoublyListNode cur = new DoublyListNode(val);
        if (head == null) {
            head = cur;
            return;
        }
        cur.next = head;
        head.prev = cur;
        head = cur;
    }
    
    public void addAtTail(int val) {
        if (head == null) {
            addAtHead(val);
            return;
        }
        
        DoublyListNode tail = getTail();
        DoublyListNode cur = new DoublyListNode(val);

        tail.next = cur;
        cur.prev = tail;
    }
    
    public void addAtIndex(int index, int val) {
        if (index == 0) {
            addAtHead(val);
            return;
        }
        
        DoublyListNode prev = getNode(index - 1);
        if (prev == null) return;
        
        DoublyListNode next = prev.next;
        DoublyListNode cur = new DoublyListNode(val);
       
        cur.next = next;
        cur.prev = prev;
        
        prev.next = cur;
        if (next != null) next.prev = cur;
    }
    
    public void deleteAtIndex(int index) {

        DoublyListNode cur = getNode(index);
        if (cur == null) return;
        DoublyListNode prev = cur.prev;
        DoublyListNode next = cur.next;
        
        if (prev == null) {
            head = next;
        } else {
            prev.next = next;
        }
        if (next != null) {
            next.prev = prev;
        }
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