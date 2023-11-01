# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hset = {}
        res = []

        def traverse(root):
            if not root: return
            
            if root.val in hset:
                hset[root.val] += 1
            else:
                hset[root.val] = 1
            
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        maximum = max(list(hset.values()))
        for key, val in hset.items():
            if val == maximum:
                res.append(key)
        return res



        