class Solution:
    def checkChildrenSum(self, root: TreeNode) -> bool:
        # Your code goes here
        if not root: return
        child=0
        if root.left:
            child+=root.left.val
        if root.right:
            child+=root.right.val

        if child>=root.val:
            root.val=child
        else:
            if root.left:
                root.left.val=root.val
            elif root.right:
                root.right.val=root.val
        self.checkChildrenSum(root.left)
        self.checkChildrenSum(root.right)
        tot=0
        if root.left:
            tot+=root.left.val
        if root.right:
            tot+=root.right.val

        if root.left or root.right:
            root.val=tot

# TC -> O(N)
# SC -> O(H)