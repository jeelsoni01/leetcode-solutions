class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        col0 = True

        # Mark rows and columns
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = False

            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Process matrix from bottom-right
        for i in range(m - 1, 0, -1):
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if not col0:
                matrix[i][0] = 0

        # Process first row
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        # Process first column
        if not col0:
            for i in range(m):
                matrix[i][0] = 0