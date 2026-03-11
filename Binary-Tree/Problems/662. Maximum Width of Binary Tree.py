# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append((root, 0))
        max_width = 0

        while q:
            level_length = len(q)
            _, level_head_index = q[0]  # First index in the level
            for _ in range(level_length):
                node, idx = q.popleft()
                curr_index = idx - level_head_index  # Normalize index
                if node.left:
                    q.append((node.left, 2 * curr_index + 1))
                if node.right:
                    q.append((node.right, 2 * curr_index + 2))
            # Last node index - first node index + 1
            if q:
                max_width = max(max_width, q[-1][1] - q[0][1] + 1)
            else:
                max_width = max(max_width, 1)

        return max_width

