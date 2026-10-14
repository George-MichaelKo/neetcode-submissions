from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh_count = 0
        q = deque()
        #track fresh count and add rotten to fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        minute = 0
        if fresh_count == 0:
            return minute
        while q and fresh_count > 0:
            minute += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if nr >=  0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        fresh_count -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))

        if fresh_count != 0:
            return -1
        return minute

                
