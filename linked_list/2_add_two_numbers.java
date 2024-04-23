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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(-1);
        ListNode cur = res;
        int x = 0, y = 0, sum = 0, carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            x = (l1 != null) ? l1.val : 0;
            y = (l2 != null) ? l2.val : 0;
            sum = x + y + carry;
            carry = sum / 10;

            cur.next = new ListNode(sum % 10);
            cur = cur.next;

            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        return res.next;
    }
}