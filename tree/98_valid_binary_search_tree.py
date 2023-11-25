# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, min_val = float('-inf'), max_val = float('inf')):
            if root == None: return True
            if not (min_val < root.val < max_val): return False

            return helper(root.left, min_val, root.val) and helper(root.right, root.val, max_val)
        return helper(root)
        