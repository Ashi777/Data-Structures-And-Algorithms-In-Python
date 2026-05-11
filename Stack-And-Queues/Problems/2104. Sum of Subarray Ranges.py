from typing import List


class Solution:
    def subArrayRanges(self, nums):
        return self.sumSubarrayMaxs(nums) - self.sumSubarrayMins(nums)

    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10 ** 9 + 7

        nse = self.nextSmallerElements(arr)
        pse = self.previousSmallerElements(arr)

        total = 0
        for i in range(n):
            left = i - pse[i]  # distance to prev smaller
            right = nse[i] - i  # distance to next smaller
            total = (total + arr[i] * left * right)
        return total

    def sumSubarrayMaxs(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10 ** 9 + 7

        nge = self.nextGreaterElements(arr)
        pge = self.previousGreaterElements(arr)

        total = 0
        for i in range(n):
            left = i - pge[i]  # distance to prev greater
            right = nge[i] - i  # distance to next greater
            total = (total + arr[i] * left * right)
        return total

    def nextSmallerElements(self, arr: List[int]) -> List[int]:
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

    def previousSmallerElements(self, arr: List[int]) -> List[int]:
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

    def nextGreaterElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        stack = []
        next_greater = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                next_greater[i] = stack[-1]
            stack.append(i)
        return next_greater

    def previousGreaterElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        stack = []
        previous_greater = [-1] * n
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                previous_greater[i] = stack[-1]
            stack.append(i)
        return previous_greater


# Example usage
sol = Solution()
print(sol.subArrayRanges([1, 2, 3]))
print(sol.subArrayRanges([1, 3, 3]))
print(sol.subArrayRanges([4, -2, -3, 4, 1]))

# TC -> O(10N)
# TC -> O(10N)
