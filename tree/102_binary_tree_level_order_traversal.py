# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# approach 1 using basic syntax
class Solution:
    def height(self, root):
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

    def treeLevelAt(self, root: Optional[TreeNode], i: int):
        if not root:
            return []
        if i == 1:
            return [root.val]
        elif i > 1:
            left = self.treeLevelAt(root.left, i - 1)
            right = self.treeLevelAt(root.right, i - 1)
            return left + right

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        n = self.height(root)
        res = []
        for i in range(1, n+1):
            res.append(self.treeLevelAt(root, i))
        return res
        
# approach using deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        while q:
            temp = []
            for i in range(len(q)):
                popped = q.popleft()
                if popped:
                    temp.append(popped.val)
                    q.append(popped.left)
                    q.append(popped.right)
            if temp:
                res.append(temp)
        return res
# approach 3 using BFS
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        res, curr = [[root.val]] , [root]
        while curr:
            next, vals = [] , []
            for node in curr:
                if node.left:
                    next.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    next.append(node.right)
                    vals.append(node.right.val)
            if next:
                curr = next.copy()
                res.append(vals)
            else:
                break
        return res