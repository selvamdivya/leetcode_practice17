class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        currentRow = 0
        direction = -1

        for ch in s:
            rows[currentRow] += ch

            if currentRow == 0 or currentRow == numRows - 1:
                direction *= -1

            currentRow += direction

        return "".join(rows)