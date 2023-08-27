# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result, marker = ListNode()
        remainder = 0

        while l1 or l2:
            x = l1.val
            y = l2.val

            summ = x + y + remainder
            if summ < 10:
                result.val = summ
                result = result.next
            else:
                deno = summ % 10
                remainder = summ // 10
                result.val = deno
                result = result.next

            l1 = l1.next
            l2 = l2.next


        if l1:
            while l1:

        if l2:

        return marker.next