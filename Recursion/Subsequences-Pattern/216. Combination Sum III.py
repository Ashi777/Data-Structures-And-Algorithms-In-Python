from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, curr, total):
            # Base case: if we used k numbers and sum == n
            if len(curr) == k and total == n:
                res.append(curr[:])
                return
            if len(curr) > k or total > n:
                return  # prune invalid cases

            for num in range(start, 10):  # only numbers 1–9
                curr.append(num)
                backtrack(num + 1, curr, total + num)  # move to next number
                curr.pop()

        backtrack(1, [], 0)
        return res


