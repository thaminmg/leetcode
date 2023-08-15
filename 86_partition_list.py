# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        ltail, rtail = left, right

        while head:
            if head.val < x:
                left.next = head
                ltail = ltail.next
            else:
                right.next = head
                rtail = rtail.next
            head = head.next
        ltail.next = right.next
        rtail.next = None
        return left.next

head = [1,4,3,2,5,2]
x = 3
print(Solution().partition(head, x))