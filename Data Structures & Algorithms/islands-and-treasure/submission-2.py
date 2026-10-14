from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c,0))
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            r,c,dist = q.popleft()
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != 2147483647:
                    continue
                    
                grid[nr][nc] = dist+1
                q.append((nr,nc,dist+1)) 
       

        
        