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
    public void reorderList(ListNode head) {
        if (head == null) return;

        ListNode firstEnd = endOfFirstHalf(head);
        ListNode secondStart = reverseSecondHalf(firstEnd.next);
        firstEnd.next = null;

        ListNode p1 = head;
        ListNode p2 = secondStart;
        ListNode temp;
        while (p2 != null) {
            temp = p1.next;
            p1.next = p2;
            p1 = temp;

            temp = p2.next;
            p2.next = p1;
            p2 = temp;
        }
    }

    ListNode reverseSecondHalf(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    ListNode endOfFirstHalf(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }
}