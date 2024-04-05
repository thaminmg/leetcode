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
    public boolean isPalindrome(ListNode head) {
        // head = [1,2,2,1] -> true, head = [1,2] -> false
        if (head == null || head.next == null) return true;
        
        int[] arr = new int[100_000];
        int i = 0;
        while(head != null) {
            arr[i++] = head.val;
            head = head.next;
        }
        
        int range = i / 2;
        for (int j = 0; j < range; j++) {
            if (arr[j] != arr[--i]) return false;
        }
        return true;
        // O(N) + O(N)
    }
    
    public boolean isPalindrome(ListNode head) {
        // head = [1,2,2,1] -> true, head = [1,2] -> false
        if (head == null || head.next == null) return true;

        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode firstEnd = slow;
        ListNode secondStart = reverse(firstEnd.next);
        
        ListNode p1 = head, p2 = secondStart;
        while (p2 != null) {
            if (p1.val != p2.val) return false;
            p1 = p1.next;
            p2 = p2.next;
        }
        firstEnd.next = reverse(secondStart);
        return true;
        // O(N) + O(N)
    }
}

// public ListNode reverse(ListNode head) {
//         ListNode prev = null, temp = null;
//         ListNode curr = head;
        
//         while (curr != null) {
//             temp = curr.next;
//             curr.next = prev;
//             prev = curr;
//             curr = temp;
//         }
//         return prev;
//     }