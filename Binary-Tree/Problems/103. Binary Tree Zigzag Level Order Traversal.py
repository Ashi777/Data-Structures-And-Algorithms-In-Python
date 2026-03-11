# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root: return res
        q=deque()
        q.append(root)
        leftToRight=True
        while q:
            size=len(q)
            row=[0]*size
            for i in range(size):
                node=q.popleft()
                index=i if leftToRight else (size-1-i)
                row[index]=node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            leftToRight= not leftToRight
            res.append(row)
        return res

