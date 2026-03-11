# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap={val: idx for idx, val in enumerate(inorder)}
        root=self._buildTree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)
        return root

    def _buildTree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
        if preStart>preEnd or inStart>inEnd:
            return None
        root=TreeNode(preorder[preStart])
        inRoot=inMap[root.val]
        numsLeft=inRoot-inStart
        root.left= self._buildTree(preorder, preStart+1, preStart+numsLeft, inorder, inStart, inRoot-1, inMap)
        root.right= self._buildTree(preorder, preStart+numsLeft+1, preEnd, inorder, inRoot+1, inEnd, inMap)
        return root

# TC -> O(N)
# SC -> O(N)