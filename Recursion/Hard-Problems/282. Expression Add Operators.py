from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)

        def backtrack(index, expr, value, last):
            # Base case: reached end of string
            if index == n:
                if value == target:
                    res.append(expr)
                return

            # Try all possible splits for the next number
            for i in range(index, n):
                # skip numbers with leading zero
                if i > index and num[index] == "0":
                    break

                curr_str = num[index:i+1]
                curr_num = int(curr_str)

                if index == 0:
                    # first number, start the expression
                    backtrack(i+1, curr_str, curr_num, curr_num)
                else:
                    # +
                    backtrack(i+1, expr + "+" + curr_str, value + curr_num, curr_num)
                    # -
                    backtrack(i+1, expr + "-" + curr_str, value - curr_num, -curr_num)
                    # *
                    backtrack(i+1, expr + "*" + curr_str, value - last + last * curr_num, last * curr_num)

        backtrack(0, "", 0, 0)
        return res
