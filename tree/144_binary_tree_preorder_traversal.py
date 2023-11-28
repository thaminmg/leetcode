# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative
        stack, res = [(root, False)], []
        while stack:
            node, visited = stack.pop()
            if node is not None:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return res


        # recursive
        # res = []
        # def dfs(root):
        #     nonlocal res
        #     if root is None: return

        #     res.append(root.val)
        #     if root.left is not None:
        #         dfs(root.left)
        #     if root.right is not None:
        #         dfs(root.right)
        # dfs(root)
        # return res
        