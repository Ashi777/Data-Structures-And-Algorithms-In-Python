class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix);
        m = len(matrix[0])
        maxArea = 0;
        pSum = [[0] * m for _ in range(n)]
        for j in range(m):
            sum1 = 0
            for i in range(n):
                if matrix[i][j] == "1":
                    sum1 += 1
                else:
                    sum1 = 0
                pSum[i][j] = sum1
        for i in range(n):
            maxArea = max(maxArea, self.largestRectangleArea(pSum[i]))
        return maxArea

    def largestRectangleArea(self, heights):
        stack = [];
        n = len(heights);
        maxArea = 0
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                element = stack.pop()
                nse = i
                pse = -1 if not stack else stack[-1]
                maxArea = max(maxArea, heights[element] * (nse - pse - 1))
            stack.append(i)
        while stack:
            nse = n
            element = stack.pop()
            pse = -1 if not stack else stack[-1]
            maxArea = max(maxArea, heights[element] * (nse - pse - 1))
        return maxArea


'''
# Example usage
sol = Solution()
print(sol.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))   
print(sol.maximalRectangle([["0"]]))
print(sol.maximalRectangle([["1"]]))

# TC -> O(M*N)+O(N*2M)
# TC -> O(M*N)+O(N)
'''

