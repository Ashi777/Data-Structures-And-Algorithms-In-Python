# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')
        self.maxPathDown(root)
        return self.maxi

    def maxPathDown(self, root):
        if not root: return 0
        left=max(0, self.maxPathDown(root.left))
        right=max(0, self.maxPathDown(root.right))
        self.maxi=max(self.maxi, left+right+root.val)
        return max(right, left)+root.val

