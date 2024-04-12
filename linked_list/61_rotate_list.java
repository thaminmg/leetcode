/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;
        int n = 0;
        ListNode cur = head;
        for (n = 1; cur.next != null; n++) {
            cur = cur.next;
        }
        k %= n;
        if (k == 0) return head;
        cur.next = head;

        int counter = 0;
        cur = head;
        while (counter < n - k - 1) {
            cur = cur.next;
            counter++;
        }
        ListNode start = cur.next;
        cur.next = null;
        
        return start;
    }
}