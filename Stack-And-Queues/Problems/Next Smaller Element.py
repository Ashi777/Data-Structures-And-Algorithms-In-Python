from typing import List

class Solution:
    def nextSmallerElements(self, arr):
        n = len(arr)
        stack = []
        next_smaller = [-1] * n

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(arr[i])

        return next_smaller

'''
# Example usage
sol = Solution()
print(sol.nextSmallerElements([4, 8, 5, 2, 25]))  # [2, 5, 2, -1, -1]
print(sol.nextSmallerElements([10, 9, 8, 7]))     # [9, 8, 7, -1]
'''