# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next    
        slow.next = None

        prev = None
        curr = second
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
    
        curr1, curr2 = head, prev

        while curr2:
            temp1, temp2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = temp1
            curr1, curr2 = temp1, temp2




        
            



        