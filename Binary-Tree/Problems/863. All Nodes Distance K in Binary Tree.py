# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        # Step 1: Build the graph (undirected)
        def buildGraph(node, parent):
            if not node:
                return
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            buildGraph(node.left, node)
            buildGraph(node.right, node)

        buildGraph(root, None)

        # Step 2: BFS from target node
        visited = set()
        queue = deque()
        queue.append((target.val, 0))  # (node_value, current_distance)
        visited.add(target.val)
        res = []

        while queue:
            node, dist = queue.popleft()
            if dist == k:
                res.append(node)
            elif dist < k:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))

        return res

