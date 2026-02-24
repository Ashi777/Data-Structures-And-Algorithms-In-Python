# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.ValidBST(root, float('-inf'), float('inf'))

    def ValidBST(self, root, minVal, maxVal):
        if not root: return True
        if (root.val >= maxVal) or (root.val <= minVal): return False
        return self.ValidBST(root.left, minVal, root.val) and self.ValidBST(root.right, root.val, maxVal)

# TC -> O(N)
# SC -> O(1)