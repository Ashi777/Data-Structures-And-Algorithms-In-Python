from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(0, [], nums)
        return self.res

    def backtrack(self, i, curr, nums):
            # Base case: if we’ve considered all elements
            if i == len(nums):
                self.res.append(curr[:])  # make a copy
                return
            # Choice 1: Exclude nums[i]
            self.backtrack(i + 1, curr, nums)
            # Choice 2: Include nums[i]
            curr.append(nums[i])
            self.backtrack(i + 1, curr, nums)
            # Backtrack (undo choice)
            curr.pop()

