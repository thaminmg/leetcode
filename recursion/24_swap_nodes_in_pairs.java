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
    
    public ListNode helper(ListNode head) {
        
        if (head == null || head.next == null) return head;
        
        ListNode first = head;
        ListNode second = head.next;

        int temp = head.val;
        head.val = second.val;
        second.val = temp;
        second.next = helper(head.next.next);
        return first;
    }
    
    public ListNode swapPairs(ListNode head) {
        return helper(head);
    }
}