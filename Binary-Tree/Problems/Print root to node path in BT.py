# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def allRootToLeaf(self, root):
        # your code goes here
        res = []
        path = []

        def dfs(node):
            if not node: return None
            path.append(node.data)
            if not node.left and not node.right:
                res.append(path[:])
            else:
                dfs(node.left)
                dfs(node.right)
            path.pop()

        dfs(root)
        return res

