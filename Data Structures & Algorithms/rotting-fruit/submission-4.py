from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh_count = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    q.append((r,c,0))
        if fresh_count == 0:
            return 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            r, c, time = q.popleft()
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    q.append((nr,nc, time + 1))

                    if fresh_count == 0:
                        return time + 1
        return -1