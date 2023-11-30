# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def helper(leftIdx, rightIdx):
            if leftIdx > rightIdx:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            rootIdx = hset[val]
            root.right = helper(rootIdx + 1, rightIdx)
            root.left = helper(leftIdx, rootIdx - 1)
            return root

        hset = {val:idx for idx, val in enumerate(inorder)}

        return helper(0, len(postorder) - 1)

        