# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def succPredBST(self, root, key):
        #your code goes here
        succ=self.successor(root, key)
        pred=self.predecessor(root, key)
        return [pred.data if pred else -1, succ.data if succ else -1]

    def successor(self, root, key):
        successor=None
        while root:
            if key>=root.data:
                root=root.right
            else:
                successor=root
                root=root.left
        return successor

    def predecessor(self, root, key):
        predecessor=None
        while root:
            if key<=root.data:
                root=root.left
            else:
                predecessor=root
                root=root.right
        return predecessor

# TC -> O(H)
# SC -> O(1)