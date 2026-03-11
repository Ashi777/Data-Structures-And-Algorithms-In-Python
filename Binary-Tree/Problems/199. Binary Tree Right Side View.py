# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root):
        #your code goes here
        res=[]
        self.recursionRight(root, 0, res)
        return res

    def leftSideView(self, root):
        res=[]
        self.recursionLeft(root, 0, res)
        return res

    def recursionLeft(self, root, level, res):
        if not root: return None
        if len(res)==level:
            res.append(root.data)
        self.recursionLeft(root.left, level+1, res)
        self.recursionRight(root.right, level+1, res)

    def recursionRight(self, root, level, res):
        if not root: return None
        if len(res)==level:
            res.append(root.data)
            self.recursionRight(root.right, level+1, res)
            self.recursionLeft(root.left, level+1, res)

# TC -> O(N) 
# SC -> O(H)