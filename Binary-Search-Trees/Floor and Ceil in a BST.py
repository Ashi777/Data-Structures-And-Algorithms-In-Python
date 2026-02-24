# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def floorCeilOfBST(self, root, key):
        #your code goes here
        ceil=-1; floor=-1
        while root:
            if root.data==key:
                ceil=root.data
                floor=root.data
                return [floor,ceil]
            elif key>root.data:
                floor=root.data
                root=root.right
            else:
                ceil=root.data
                root=root.left
        return [floor,ceil]

# TC -> O(log(base2)N)