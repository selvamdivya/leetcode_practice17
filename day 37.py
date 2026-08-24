class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Store existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + c // 3].add(num)

        def solve():
            min_candidates = None
            min_row = -1
            min_col = -1

            # Find empty cell with minimum possible choices
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        box = (r // 3) * 3 + c // 3
                        candidates = []

                        for num in '123456789':
                            if (num not in rows[r] and
                                num not in cols[c] and
                                num not in boxes[box]):
                                candidates.append(num)

                        if len(candidates) == 0:
                            return False

                        if (min_candidates is None or
                                len(candidates) < len(min_candidates)):
                            min_candidates = candidates
                            min_row = r
                            min_col = c

            # No empty cells → solved
            if min_candidates is None:
                return True

            box = (min_row // 3) * 3 + min_col // 3

            for num in min_candidates:
                board[min_row][min_col] = num
                rows[min_row].add(num)
                cols[min_col].add(num)
                boxes[box].add(num)

                if solve():
                    return True

                # Backtrack
                board[min_row][min_col] = '.'
                rows[min_row].remove(num)
                cols[min_col].remove(num)
                boxes[box].remove(num)

            return False

        solve()