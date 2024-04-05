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
    public ListNode oddEvenList(ListNode head) {
        // head = [1,2,3,4,5] -> [1,3,5,2,4]
        if (head == null) return head;
        
        ListNode odd = head, even = head.next;
        ListNode res = odd, evenStart = even;

        while (even != null && even.next != null) {
            odd.next = even.next;
            odd = odd.next;
            even.next = odd.next;
            even = even.next;
        }
        odd.next = evenStart;
        return res;
        // O (N) + O (1)
    }
}
        // O (N) + O (1)
        // ListNode odd = new ListNode(0);
        // ListNode even = new ListNode(0);
        // int count = 1;
        // ListNode res = odd;
        // ListNode join = even;
        
        // while (head != null) {
        //     if ((count & 1) == 1) {
        //         odd.next = head;
        //         odd = odd.next;
        //     } else {
        //         even.next = head;
        //         even = even.next;
        //     }
        //     count++;
        //     head = head.next;
        // }
        // odd.next = join.next;
        // even.next = null;
        // return res.next;
//     }
// }