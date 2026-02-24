# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        k_smallest = [None]
        # k_largest=[None]
        counter = [0]
        self.inorder(root, counter, k, k_smallest)
        # counter=0
        # self.reverseInorder(root, counter, k, k_largest)
        return k_smallest[0]  # , k_largest[0]

    def inorder(self, root, counter, k, k_smallest):
        if not root or counter[0] >= k:
            return None
        self.inorder(root.left, counter, k, k_smallest)
        counter[0] += 1
        if counter[0] == k:
            k_smallest[0] = root.val
            return None
        self.inorder(root.right, counter, k, k_smallest)


'''    def reverseInorder(self, root, counter, k, k_largest):
        if not root or counter[0]>=k:
            return None
        self.reverseInorder(root.right, counter, k, k_largest)
        counter[0]+=1
        if counter[0]==k:
            k_largest[0]=root.val
            return None
        self.reverseInorder(root.left, counter, k, k_largest)
        '''
