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
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()  
                if i < n - 1:
                    node.next = q[0]
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root

        # if not root: return root
        
        # leftmost = root
        
        # while leftmost:
        #     head = leftmost
            
        #     while head:          
        #         print(head.val)    
        #         if head.left and head.right:
        #             head.left.next = head.right
        #         if head.right and head.next:
        #             if  head.next.left:
        #                 head.right.next = head.next.left
        #             elif head.next.right:
        #                 head.right.next = head.next.right
        #         elif head.left and head.next:
        #             if head.next.left:
        #                 head.left.next = head.next.left
        #             elif head.next.right:
        #                 head.left.next = head.next.right
                    
        #         head = head.next
                
        #     leftmost = leftmost.left
        # return root
        