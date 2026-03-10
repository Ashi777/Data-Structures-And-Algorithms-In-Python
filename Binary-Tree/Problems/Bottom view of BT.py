# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def bottomView(self, root):
        #your code goes here
        ans=[]
        if not root: return ans
        mpp={}
        q=deque([(root, 0)])
        while q:
            node, line=q.popleft()
            mpp[line]=node.data
            if node.left:
                q.append((node.left, line-1))
            if node.right:
                q.append((node.right, line+1))
        for value in sorted(mpp.items()):
            ans.append(value[1])
        return ans

