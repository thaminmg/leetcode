# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None # disconnect
        # reversing
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # merging
        first, second = head, prev
        result = ListNode()
        while first and first.next:
            result.next = first
            result = result.next



    

        


def convert_to_linked_list(input_list):
    head = None
    for i in range(len(input_list) - 1, -1, -1):
        new_head = ListNode(input_list[i], head)
        head = new_head
    return head

head = [1,2,3,4]
print(Solution().reorderList(convert_to_linked_list(head)))