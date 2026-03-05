class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    empty.append((i, j))
                else:
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[(i // 3) * 3 + (j // 3)].add(ch)

        def possible_digits(i, j):
            b = (i // 3) * 3 + (j // 3)
            return set('123456789') - rows[i] - cols[j] - boxes[b]

        # Step 1: Sort empty cells by fewest options (MRV heuristic)
        empty.sort(key=lambda pos: len(possible_digits(pos[0], pos[1])))

        def backtrack(index):
            if index == len(empty):
                return True

            i, j = empty[index]
            b = (i // 3) * 3 + (j // 3)

            for ch in possible_digits(i, j):  # only try valid digits
                board[i][j] = ch
                rows[i].add(ch)
                cols[j].add(ch)
                boxes[b].add(ch)

                if backtrack(index + 1):
                    return True

                board[i][j] = '.'
                rows[i].remove(ch)
                cols[j].remove(ch)
                boxes[b].remove(ch)

            return False

        backtrack(0)

