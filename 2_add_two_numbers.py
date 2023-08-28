# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = marker = ListNode()
        remainder = 0

        while l1 and l2:
            x = l1.val
            y = l2.val

            summ = x + y + remainder
            if summ < 10:
                result.next = ListNode(summ)
                result = result.next
                remainder = 0
            else:
                deno = summ % 10
                remainder = summ // 10
                result.next = ListNode(deno)
                result = result.next

            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                summ = l1.val + remainder
                if summ < 10:
                    result.next = ListNode(summ)
                    result = result.next
                    remainder = 0
                else:
                    deno = summ % 10
                    remainder = summ // 10
                    result.next = ListNode(deno)
                    result = result.next
                l1 = l1.next

        if l2:
            while l2:
                summ = l2.val + remainder
                if summ < 10:
                    result.next = ListNode(summ)
                    result = result.next
                    remainder = 0
                else:
                    deno = summ % 10
                    remainder = summ // 10
                    result.next = ListNode(deno)
                    result = result.next
                l2 = l2.next
        if remainder > 0:
            result.next = ListNode(remainder)
            result = result.next
            result.next = None


        return marker.next