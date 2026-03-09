# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [];
        stack = [];
        current = root
        last_visited = None
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                if peek_node.right and peek_node.right != last_visited:
                    current = peek_node.right
                else:
                    res.append(peek_node.val)
                    last_visited = stack.pop()
        return res

# TC -> O(2N)
# SC -> O(N)