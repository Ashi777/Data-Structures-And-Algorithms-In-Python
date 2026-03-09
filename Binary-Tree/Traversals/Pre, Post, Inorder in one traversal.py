# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def tree_traversal(self, root):
        #your code goes here
        pre, inorder, post = [], [], []
        if not root: return []
        stack=[(root, 1)]
        while stack:
            node, state=stack.pop()
            if state==1:
                pre.append(node.data)
                state=2
                stack.append((node, state))
                if node.left:
                    stack.append((node.left, 1))
            elif state==2:
                inorder.append(node.data)
                state=3
                stack.append((node, state))
                if node.right:
                    stack.append((node.right, 1))
            else:
                post.append(node.data)
        return [inorder, pre, post]

# TC -> O(3N)
# SC -> O(4N)