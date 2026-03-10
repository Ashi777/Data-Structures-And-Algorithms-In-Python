# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def boundary(self, root):
        #your code goes here
        res=[]
        if not root: return res
        if not self.isLeaf(root): res.append(root.data)
        self.addLeftBoundary(root, res)
        self.addLeaves(root, res)
        self.addRightBoundary(root, res)
        return res

    def isLeaf(self, root):
        return not root.left and not root.right

    def addLeftBoundary(self, root, res):
        curr=root.left
        while curr:
            if not self.isLeaf(curr): res.append(curr.data)
            if curr.left: curr=curr.left
            else: curr=curr.right

    def addRightBoundary(self, root, res):
        curr=root.right
        temp=[]
        while curr:
            if not self.isLeaf(curr): temp.append(curr.data)
            if curr.right: curr=curr.right
            else: curr=curr.left
        for i in range(len(temp)-1, -1, -1):
            res.append(temp[i])

    def addLeaves(self, root, res):
        if self.isLeaf(root):
            res.append(root.data)
            return
        if root.left: self.addLeaves(root.left, res)
        if root.right: self.addLeaves(root.right, res)

