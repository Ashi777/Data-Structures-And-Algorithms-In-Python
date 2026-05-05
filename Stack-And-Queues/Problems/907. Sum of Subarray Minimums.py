from typing import List


class Solution:

    def sumSubarrayMins(self, arr):
        nse = self.nextSmallerElements(arr)
        pse = self.previousSmallerElements(arr)
        n = len(arr);
        total = 0;
        mod = int(1e9 + 7)
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            total = (total + (right * left * arr[i])) % mod
        return total

    def nextSmallerElements(self, arr):
        n = len(arr)
        stack = []
        next_smaller = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)
        return next_smaller

    def previousSmallerElements(self, arr):
        n = len(arr)
        stack = []
        previous_smaller = [-1] * n
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                previous_smaller[i] = stack[-1]
            stack.append(i)
        return previous_smaller


# Example usage
sol = Solution()
print(sol.sumSubarrayMins([3, 1, 2, 4]))
print(sol.sumSubarrayMins([11, 81, 94, 43, 3]))

# TC -> O(5N)
# TC -> O(5N)