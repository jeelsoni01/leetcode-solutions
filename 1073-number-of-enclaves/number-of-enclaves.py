class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return

            grid[r][c] = 0
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(m):
            if grid[r][0]:
                dfs(r, 0)
            if grid[r][n - 1]:
                dfs(r, n - 1)

        for c in range(n):
            if grid[0][c]:
                dfs(0, c)
            if grid[m - 1][c]:
                dfs(m - 1, c)

        return sum(cell for row in grid for cell in row)