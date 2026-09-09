class Solution:
    def totalNQueens(self, n):
        self.count = 0
        board = [["."] * n for _ in range(n)]

        def isSafe(row, col):
            # Check column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check left diagonal
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check right diagonal
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def backtrack(row):
            if row == n:
                self.count += 1
                return

            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"

                    backtrack(row + 1)

                    board[row][col] = "."

        backtrack(0)

        return self.count