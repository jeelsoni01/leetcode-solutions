class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, n - 1

        while left <= right:
            col = (left + right) // 2

            row = 0
            for i in range(1, m):
                if mat[i][col] > mat[row][col]:
                    row = i

            left_val = mat[row][col - 1] if col > 0 else -1
            right_val = mat[row][col + 1] if col < n - 1 else -1

            if mat[row][col] > left_val and mat[row][col] > right_val:
                return [row, col]

            if left_val > mat[row][col]:
                right = col - 1
            else:
                left = col + 1