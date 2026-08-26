class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if r >= rows or r < 0  or c >= cols or c < 0 or grid[r][c] == 0:
                return 0
            if grid[r][c] == 1:
                grid[r][c] = 0
            #right
            right = dfs(r,c+1)
            #left
            left = dfs(r,c-1)
            #up
            up = dfs(r+1,c)
            #down
            down = dfs(r-1,c)
            return left + right + up + down + 1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    currArea = dfs(r,c)
                    maxArea =  max(currArea, maxArea)
        return maxArea   
            
        