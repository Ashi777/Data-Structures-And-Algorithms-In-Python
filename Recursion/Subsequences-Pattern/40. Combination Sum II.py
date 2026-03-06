class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        candidates.sort()

        def findCombination(ind, target):
            if target == 0:
                ans.append(ds[:])
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                findCombination(i + 1, target - candidates[i])
                ds.pop()

        findCombination(0, target)
        return ans


'''
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # sort to handle duplicates easily

        def backtrack(start, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                # Skip duplicate numbers at the same recursion level
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])  # move to next index (use once)
                curr.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return res
'''