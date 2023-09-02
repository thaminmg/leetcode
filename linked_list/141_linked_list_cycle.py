# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

def convert_to_linked_list(input_list):
    head = None
    for i in range(len(input_list) - 1, -1, -1):
        new_head = ListNode(input_list[i], head)
        head = new_head
    return head

head = [3,2,0,-4]
pos = 1
print(Solution().hasCycle(convert_to_linked_list(head)))