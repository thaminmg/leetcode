# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow

        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while head and prev:
            if head.val == prev.val:
                head = head.next
                prev = prev.next
            else:
                return False
        return True



        