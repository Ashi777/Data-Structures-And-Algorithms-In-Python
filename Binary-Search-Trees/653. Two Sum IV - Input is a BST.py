# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root, isReverse):
        self.stack=[]
        self.reverse=isReverse
        self.pushAll(root)

    def hasNext(self):
        return len(self.stack)>0

    def next(self):
        tempNode=self.stack.pop()
        if not self.reverse:
            self.pushAll(tempNode.right)
        else:
            self.pushAll(tempNode.left)
        return tempNode.val

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            if self.reverse==True:
                node=node.right
            else:
                node=node.left

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root: return False
        l=BSTIterator(root, False)
        r=BSTIterator(root, True)
        i=l.next()
        j=r.next()
        while(i<j):
            if (i+j==k): return True
            elif (i+j<k): i=l.next()
            else: j=r.next()
        return False

