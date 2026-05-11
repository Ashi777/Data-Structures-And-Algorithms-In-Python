class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):  # traverse from right to left
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(arr[i])

        return res


# Example usage:
sol = Solution()
print(sol.nextLargerElement([1, 3, 2, 4]))  # [3, 4, 4, -1]
print(sol.nextLargerElement([6, 8, 0, 1, 3]))  # [8, -1, 1, 3, -1]

# TC->O(2N)
# SC->O(N)