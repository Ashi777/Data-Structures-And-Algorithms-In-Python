from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, curr, total):
            # Base cases
            if total == target:
                res.append(curr[:])  # found a valid combination
                return
            if total > target:
                return

            # Explore choices
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                # We pass `i` not `i+1` because we can reuse same element
                backtrack(i, curr, total + candidates[i])
                curr.pop()  # backtrack

        backtrack(0, [], 0)
        return res
