# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if not root:
            return 0
        
        lheight = self.height(root.left)
        rheight = self.height(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root)
        