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
    public ListNode mergeNodes(ListNode head) {
        ListNode og = head;
        ListNode res = new ListNode();
        ListNode curr = res;

        int sum = 0;
        while (head.next != null) {
            if (head.next.val != 0) {
                sum += head.next.val;
            } else {
                curr.next = new ListNode(sum);
                curr = curr.next;
                sum = 0;
            }
            head = head.next;
        }
        return res.next;
    }
}