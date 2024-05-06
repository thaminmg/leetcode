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

    public ListNode removeNodes(ListNode head) {
        Stack<Integer> stack = new Stack<>();
        ListNode curr = head;

        while (curr != null) {
            stack.push(curr.val);
            curr = curr.next;
        }
        int current = stack.pop();
        int maximum = current;
        ListNode res = new ListNode(maximum);

        while (!stack.isEmpty()) {
            current = stack.pop();
            if (current < maximum) {
                continue;
            } else {
                ListNode newNode = new ListNode(current);
                newNode.next = res;
                res = newNode;
                maximum = Math.max(maximum, current);
            }
        }
        return res;
    }
}