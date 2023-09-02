# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print(head)
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev




head = [1,2,3,4,5]
print(Solution().reverseList(head))