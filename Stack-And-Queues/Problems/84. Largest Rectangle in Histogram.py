class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
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


# Example usage
sol = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(sol.largestRectangleArea([2, 4]))

# TC -> O(2N)
# TC -> O(N)

