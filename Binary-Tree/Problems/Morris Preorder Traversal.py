# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, root):
        #your code goes here
        preorder = []
        curr = root
        while curr:
            if not curr.left:
                preorder.append(curr.data)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    preorder.append(curr.data)  # Add before going to left
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
        return preorder

