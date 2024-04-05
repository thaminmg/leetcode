class Solution {
    public ListNode removeElements(ListNode head, int val) {
        // head = [1,2,6,3,4,5,6], val = 6 -> [1,2,3,4,5]
        ListNode res = new ListNode(0);
        ListNode prev = res;
        
        while (head != null) {
            if (head.val != val) {
                prev.next = head;
                prev = prev.next;
            }
            head = head.next;
        }
        prev.next = null;
        return res.next;
        // O(N) + O(1)
    }
}