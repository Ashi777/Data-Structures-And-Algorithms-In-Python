# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i=0
        return self.build(preorder, float('inf'))

    def build(self, preorder, bound):
        if self.i==len(preorder) or preorder[self.i]>bound: return None
        root_val=preorder[self.i]
        self.i+=1
        root=TreeNode(root_val)
        root.left=self.build(preorder, root_val)
        root.right=self.build(preorder, bound)
        return root

# TC -> O(3N)
# SC -> O(1)