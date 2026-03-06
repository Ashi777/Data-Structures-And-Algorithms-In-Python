from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # Mapping of digits to letters
        self.phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        self.res = []
        self.backtrack(0, [], digits)
        return self.res

    def backtrack(self, index, path, digits):
        # Base case: if the path length == digits length
        if index == len(digits):
            self.res.append("".join(path))
            return

        # Get possible letters for current digit
        for ch in self.phone_map[digits[index]]:
            path.append(ch)            # choose
            self.backtrack(index + 1, path, digits) # explore
            path.pop()                 # undo choice


