# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break # collision happens, not the start of loop

        # check if it contains no loop
        if not fast.next or not fast.next.next: return

        # move fast runner to head and runs agains, after k nodes, collision will happens at the start of loop
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
        