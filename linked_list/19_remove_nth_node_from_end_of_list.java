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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // head = [1,2,3,4,5], n = 2 -> [1,2,3,5]
        ListNode res = new ListNode(0);
        res.next = head;
        int length = 0;
        while (head != null) {
            length++;
            head = head.next;
        }
        length -= n;
        
        ListNode first = res;
        while (length > 0) {
            length--;
            first = first.next;
        }
        first.next = first.next.next;
        return res.next;
        // O(N) + O(1)
    }
}