class Solution:
    def reverse(self, arr, n):
        self.helper(arr, 0, n - 1)

    def helper(self, arr, start, end):
        if start >= end:
            return
        arr[start], arr[end] = arr[end], arr[start]
        self.helper(arr, start + 1, end - 1)

