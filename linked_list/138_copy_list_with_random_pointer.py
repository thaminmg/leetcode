"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        marker = head
        hset = {}
        
        while marker:
            hset[marker] = Node(marker.val)
            marker = marker.next

        marker = head
        while marker:
            hset[marker].next = hset.get(marker.next)
            hset[marker].random = hset.get(marker.random)
            marker = marker.next
            
        return hset[head]
        