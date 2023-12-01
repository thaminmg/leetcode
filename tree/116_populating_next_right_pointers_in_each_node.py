"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        deq = deque([(root, 0)])
        prev = None
        while deq:
            temp = deq.popleft()
            if temp and temp[0].left and temp[0].right:
                temp[0].left.next = temp[0].right 
                
                if prev and prev[1] == temp[1] + 1:
                    prev[0].next = temp[0].left 
                prev = (temp[0].right, temp[1]+1)
                
                deq.append((temp[0].left, temp[1]+1))
                deq.append((temp[0].right, temp[1]+1))
        return root
        