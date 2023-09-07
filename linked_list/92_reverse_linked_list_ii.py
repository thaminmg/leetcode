# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: 
            return head

        count = 1
        start = head
        marker = head
        prev = None
        previous = None
        while marker:
            if left <= count <= right:
                if previous and count == left:
                    previous.next = None
                temp = marker.next
                marker.next = prev
                prev = marker
                previous = marker
                marker = temp
            else:
                previous = marker
                marker = marker.next
            if count == right:
                temp = prev
                while prev.next:
                    prev = prev.next
                if prev:
                    prev.next = marker
                if left == 1:
                    head = temp
                else:
                    while start.next:
                        start = start.next
                    if start:
                        start.next = temp
            count += 1            
            
        return head
