from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()      # columns where queens are placed
        diag1 = set()     # r - c (↙ diagonal)
        diag2 = set()     # r + c (↘ diagonal)

        def backtrack(r):
            if r == n:
                # Found a valid board
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                # Place queen
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                # Recurse to next row
                backtrack(r + 1)

                # Backtrack
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return res

