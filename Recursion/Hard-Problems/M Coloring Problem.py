class Solution:
    def graphColoring(self, edges, m, n):
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # To store color assignment for vertices
        color = [0] * n

        def isSafe(node, c):
            # Check if any adjacent vertex has the same color
            for nei in adj[node]:
                if color[nei] == c:
                    return False
            return True

        def solve(node):
            if node == n:  # all vertices colored
                return True

            # Try all colors from 1 to m
            for c in range(1, m + 1):
                if isSafe(node, c):
                    color[node] = c
                    if solve(node + 1):  # recursive call
                        return True
                    color[node] = 0  # backtrack
            return False

        return solve(0)


