# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root):
        if not root:
            return None
        while root.left:
            root=root.left
        return root.val

    def findMin(self, root):
        if not root:
            return None
        while root.right:
            root=root.right
        return root.val

