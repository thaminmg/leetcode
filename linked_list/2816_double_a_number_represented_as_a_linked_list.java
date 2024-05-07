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
    public ListNode reverse(ListNode root) {
        ListNode curr = root;
        ListNode prev = null, next;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    public ListNode doubleIt(ListNode head) {
        ListNode reversedList = reverse(head);
        ListNode curr = reversedList, prev = null;

        int carry = 0, res = 0;

        while (curr != null) {
            res = (2 * curr.val) + carry;
            carry = res / 10;
            curr.val = res % 10;
            prev = curr;
            curr = curr.next;
        }
        if (carry > 0) {
            ListNode temp = new ListNode(carry);
            prev.next = temp;
        }
        return reverse(reversedList);
    }
}