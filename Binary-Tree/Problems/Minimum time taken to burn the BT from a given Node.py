# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def timeToBurnTree(self, root, start):
        #your code goes here
        parent_map = {}
        target_node = None

        # Step 1: Map each node to its parent and find target node
        def dfs(node, parent):
            nonlocal target_node
            if not node:
                return
            if node.data == target:
                target_node = node
            if parent:
                parent_map[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        # Step 2: BFS to simulate burning process
        visited = set()
        queue = deque()
        queue.append(target_node)
        visited.add(target_node)
        time = -1

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for neighbor in [node.left, node.right, parent_map.get(node)]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            time += 1

        return time

# TC -> O(2N)
# SC -> O(N)