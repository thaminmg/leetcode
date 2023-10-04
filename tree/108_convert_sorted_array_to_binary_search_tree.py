# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def insert(self, root, data):
    #     if data < root.val:
    #         if root.left:
    #             self.insert(root.left, data)
    #         else:
    #             root.left = TreeNode(data)
    #             return
    #     else:
    #         if root.right:
    #             self.insert(root.right, data)
    #         else:
    #             root.right = TreeNode(data)
    #             return
  
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        first = nums[:mid]
        second = nums[mid+1:]
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(first)
        root.right = self.sortedArrayToBST(second)
        return root
    
        # not optimal
        # if not nums:
        #     return None
        # mid = len(nums) // 2
        # first = nums[:mid]
        # second = nums[mid+1:]
        # root = TreeNode(nums[mid])
        # for i in first:
        #     self.insert(root, i)
        # for j in second:
        #     self.insert(root, j)

        # return root

        