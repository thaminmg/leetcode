# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListNode(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def addTwoLists(self, l1, l2):
        marker = ListNode()
        result = marker
        carry = 0
        while l1 or l2 or carry:
            operand1 = l1.val if l1 else 0
            operand2 = l2.val if l2 else 0
            summ = carry + operand1 + operand2 
            remainder = summ % 10
            carry = summ // 10
            newnode = ListNode(remainder)
            result.next = newnode
            result = result.next

            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None
        return marker.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = self.reverseListNode(l1)
        list2 = self.reverseListNode(l2)
        summ = self.addTwoLists(list1, list2)
        result = self.reverseListNode(summ)

        return result