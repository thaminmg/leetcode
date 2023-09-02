# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hset = set()
        prev = None
        mark = head
        while head:
            if head.val in hset:
                prev.next = head.next
            else:
                hset.add(head.val)
                prev = head
            head = head.next
        return mark
    
def convert_to_linked_list(input_list):
    head = None
    for i in range(len(input_list) - 1, -1, -1):
        new_head = ListNode(input_list[i], head)
        head = new_head
    return head

head = [1,1,2]
print(Solution().deleteDuplicates(convert_to_linked_list(head)))