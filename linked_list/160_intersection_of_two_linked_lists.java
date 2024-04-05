/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // headA = [4,1,8,4,5], headB = [5,6,1,8,4,5] -> [1,8,4,5] || []
        ListNode p1 = headA;
        ListNode p2 = headB;
        
        while (p1 != p2) {
            p1 = p1 == null ? headB : p1.next;
            p2 = p2 == null ? headA : p2.next;
        }
        // O (M + N) + O(1)
        return p1;
    }
}

        // O(M + N) + O (N)
        // Set<ListNode> hash = new HashSet<>();
        
        // while (headB != null) {
        //       hash.add(headB);
        //       headB = headB.next;
        //   }
        
        //   while (headA != null) {
        //       if (hash.contains(headA)) return headA;
        //       headA = headA.next;
        //   }
        //   return null;
//     }
// }