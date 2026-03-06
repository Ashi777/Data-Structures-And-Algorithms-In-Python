class Solution:
    def permute(self, arr):
        res = []
        n = len(arr)

        def backtrack(start):
            if start == n:
                res.append(arr[:])  # store a copy
                return
            for i in range(start, n):
                arr[start], arr[i] = arr[i], arr[start]  # swap
                backtrack(start + 1)  # recurse
                arr[start], arr[i] = arr[i], arr[start]  # backtrack (undo swap)

        backtrack(0)
        return res
