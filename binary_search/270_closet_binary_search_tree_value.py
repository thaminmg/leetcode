# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        res = root.val
        
        while root:
            res = min(root.val, res, key=lambda x: (abs(x - target), x))
            root = root.left if root.val > target else root.right
            
        return res
        