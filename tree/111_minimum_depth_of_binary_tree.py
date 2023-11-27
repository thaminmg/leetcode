# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if not left and not right: return 1
            if not left: return 1 + right
            if not right: return 1 + left
            
            return 1 + min(left, right)
        return dfs(root)
