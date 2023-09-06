# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        marker = head
        count = 0
        while marker:
            count += 1
            marker = marker.next
        
        parts = count // k
        remains = count % k

        result = [None] * k
        marker = head
        prev = None
        for i in range(k):
            result[i] = marker
            for j in range(parts + (1 if remains > 0 else 0)):
                prev = marker 
                marker = marker.next
            if prev:
                prev.next = None
            remains -= 1

        
        return result
            