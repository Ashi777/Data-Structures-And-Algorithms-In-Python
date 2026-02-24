# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
class NodeValue:
    def __init__(self, minNode, maxNode, maxSize):
        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize

class Solution:
    def largestBST(self, root):
        #your code goes here
        return self.largestBSTHelper(root).maxSize

    def largestBSTHelper(self, root):
        if not root:
            return NodeValue(float('inf'), float('-inf'), 0)
        left=self.largestBSTHelper(root.left)
        right=self.largestBSTHelper(root.right)
        if (left.maxNode<root.data and root.data<right.minNode):
            return NodeValue(min(root.data, left.minNode), max(root.data, right.maxNode), left.maxSize+right.maxSize+1)
        return NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))

# TC -> O(N)
# SC -> O(1)