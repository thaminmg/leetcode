# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = dummy = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                result.next = list1
                result = list1
                list1 = list1.next
            else:
                result.next = list2
                result = list2
                list2 = list2.next
        if list1 or list2:
            result.next = list1 if list2 is None else list2
        return dummy.next
        
def convert_to_linked_list(input_list):
    head = None
    for i in range(len(input_list) - 1, -1, -1):
        new_head = ListNode(input_list[i], head)
        head = new_head
    return head

list1 = [1,2,4]
list2 = [1,3,4]
list1 = []
list2 = []
list1 = []
list2 = [0]
print(Solution().mergeTwoLists(convert_to_linked_list(list1), convert_to_linked_list(list2)))

