# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(0)
        start = ListNode(0)
        start.next = head
        p1 = start
        p2 = start

        for i in range(n + 1):
            if i == None:
                return None
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next
        return start.next

def convert_to_linked_list(input_list):
    head = None
    for i in range(len(input_list) - 1, -1, -1):
        new_head = ListNode(input_list[i], head)
        head = new_head
    return head

head = [1,2,3,4,5]
n = 2
print(Solution().removeNthFromEnd(convert_to_linked_list(head) , n))