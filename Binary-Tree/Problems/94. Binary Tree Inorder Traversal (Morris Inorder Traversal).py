# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def getInorder(self, root):
        #your code goes here
        inorder=[]
        curr=root
        while curr:
            if not curr.left:
                inorder.append(curr.data)
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                if not prev.right:
                    prev.right=curr
                    curr=curr.left
                else:
                    prev.right=None
                    inorder.append(curr.data)
                    curr=curr.right
        return inorder

# TC -> O(N)
# SC -> O(1)