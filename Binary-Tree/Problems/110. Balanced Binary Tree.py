# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root):
        if not root: return 0
        leftHeight = self.dfsHeight(root.left)
        if leftHeight == -1: return -1
        rightHeight = self.dfsHeight(root.right)
        if rightHeight == -1: return -1
        if (abs(leftHeight - rightHeight)) > 1: return -1
        return (max(leftHeight, rightHeight) + 1)

# TC -> O(N)