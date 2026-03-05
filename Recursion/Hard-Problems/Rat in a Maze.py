class Solution:
    def findPath(self, grid):
        #your code goes here
        n = len(grid)
        res = []
        visited = [[False]*n for _ in range(n)]

        # Directions: Down, Left, Right, Up
        dirs = [(1,0,'D'), (0,-1,'L'), (0,1,'R'), (-1,0,'U')]

        def isSafe(x, y):
            return 0 <= x < n and 0 <= y < n and grid[x][y] == 1 and not visited[x][y]

        def backtrack(x, y, path):
            # Base case: reached destination
            if x == n-1 and y == n-1:
                res.append(path)
                return

            # Mark current cell visited
            visited[x][y] = True

            # Explore all possible moves
            for dx, dy, move in dirs:
                nx, ny = x + dx, y + dy
                if isSafe(nx, ny):
                    backtrack(nx, ny, path + move)

            # Backtrack (unmark for other paths)
            visited[x][y] = False

        if grid[0][0] == 1:
            backtrack(0, 0, "")

        return res if res else ["-1"]

