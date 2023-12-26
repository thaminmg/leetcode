"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        res = []
        queue = deque([root])

        while queue:
            temp = []

            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                queue.extend(node.children)
            res.append(temp)

        return res
        