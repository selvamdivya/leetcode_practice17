class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []
            for j in range(cols + 1):
                current = heights[j] if j < cols else 0

                while stack and heights[stack[-1]] > current:
                    height = heights[stack.pop()]
                    width = j if not stack else j - stack[-1] - 1
                    max_area = max(max_area, height * width)

                stack.append(j)

        return max_area
