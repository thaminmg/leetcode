# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative
        # stack, res = [(root, False)], []
        # while stack:
        #     node, visited = stack.pop()
        #     if node is not None:
        #         if visited:
        #             res.append(node.val)
        #         else:
        #             stack.append((node, True))
        #             stack.append((node.right, False))
        #             stack.append((node.left, False))
        # return res
        # recursive
        res = []
        def dfs(root):
            if root is None: return
            if root.left is not None: dfs(root.left)
            if root.right is not None: dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res
    
    
        