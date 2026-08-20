class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1] * n for _ in range(m)]
        for r in range(1,m):
            for c in range(1,n):
                above = grid[r-1][c]
                left = grid [r][c-1]

                grid[r][c]= above + left
        return grid[m-1][n-1]