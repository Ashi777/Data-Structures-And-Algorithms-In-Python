from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.backtrack("", n, n)
        return self.res

    def backtrack(self, curr, open_count, close_count):
        # Base case: valid sequence built
        if open_count == 0 and close_count == 0:
            self.res.append(curr)
            return

        # Option 1: place '('
        if open_count > 0:
            self.backtrack(curr + "(", open_count - 1, close_count)

        # Option 2: place ')'
        if close_count > open_count:
            self.backtrack(curr + ")", open_count, close_count - 1)

