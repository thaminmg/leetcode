# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []

        def dfs(root, lst):
            if not root: return
            if not root.left and not root.right:
                lst.append(root.val)

            dfs(root.left, lst)
            dfs(root.right, lst)    

        dfs(root1, res1)
        dfs(root2, res2)

        return res1 == res2
        