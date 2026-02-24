# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Replace with max in left subtree or min in right subtree
                maxLeft = self.getMax(root.left)
                root.val = maxLeft.val
                root.left = self.deleteNode(root.left, maxLeft.val)
        return root

    def getMax(self, node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node

